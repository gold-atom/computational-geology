from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .engine import (
    ASSAY_CONTRADICTED,
    ASSAY_INSUFFICIENT_EVIDENCE,
    ASSAY_VERIFIED,
    EVIDENCE_VERSION,
    _bundle_integrity_sha256,
    _specimen_id,
    export_evidence_bundle,
)

PROFILE_ID = "bitcoin-header-field-return/v1"
PROFILE_SUMMARY = (
    "Three consecutive runs over one Bitcoin block-header field within one declared offline header stream, "
    "labeled A->B->A where A and B differ."
)
HEADER_SIZE = 80
HEADER_ENCODING = "bitcoin-block-header-raw80-concatenated/v1"
SUPPORTED_FIELDS = {"bits", "merkle_root", "nonce", "previous_block_hash", "timestamp", "version"}


class BitcoinInspectionError(RuntimeError):
    """Raised when the declared Bitcoin header source cannot be inspected."""


@dataclass(frozen=True)
class BitcoinHeader:
    height: int
    raw_header_hex: str
    block_hash: str
    previous_block_hash: str
    merkle_root: str
    version: int
    timestamp: int
    bits: str
    nonce: int


@dataclass(frozen=True)
class HeaderRun:
    value: int | str
    start_height: int
    end_height: int
    start_block_hash: str


def _sha256d(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def _display_hash(little_endian_bytes: bytes) -> str:
    return little_endian_bytes[::-1].hex()


def serialize_block_header(
    *,
    version: int,
    previous_block_hash: str,
    merkle_root: str,
    timestamp: int,
    bits: str,
    nonce: int,
) -> bytes:
    return b"".join(
        [
            version.to_bytes(4, "little", signed=True),
            bytes.fromhex(previous_block_hash)[::-1],
            bytes.fromhex(merkle_root)[::-1],
            timestamp.to_bytes(4, "little"),
            int(bits, 16).to_bytes(4, "little"),
            nonce.to_bytes(4, "little"),
        ]
    )


def read_block_headers(headers_file: str | Path, *, start_height: int = 0) -> list[BitcoinHeader]:
    if start_height < 0:
        raise ValueError("start_height must be non-negative")
    header_path = Path(headers_file)
    content = header_path.read_bytes()
    if len(content) % HEADER_SIZE != 0:
        raise BitcoinInspectionError("header file length is not a multiple of 80 bytes")

    headers: list[BitcoinHeader] = []
    for index in range(0, len(content), HEADER_SIZE):
        raw_header = content[index : index + HEADER_SIZE]
        height = start_height + (index // HEADER_SIZE)
        headers.append(
            BitcoinHeader(
                height=height,
                raw_header_hex=raw_header.hex(),
                block_hash=_display_hash(_sha256d(raw_header)),
                previous_block_hash=_display_hash(raw_header[4:36]),
                merkle_root=_display_hash(raw_header[36:68]),
                version=int.from_bytes(raw_header[0:4], "little", signed=True),
                timestamp=int.from_bytes(raw_header[68:72], "little"),
                bits=f"{int.from_bytes(raw_header[72:76], 'little'):08x}",
                nonce=int.from_bytes(raw_header[76:80], "little"),
            )
        )

    _validate_header_chain(headers)
    return headers


def _validate_header_chain(headers: list[BitcoinHeader]) -> None:
    if not headers:
        return
    for previous_header, current_header in zip(headers, headers[1:]):
        if current_header.previous_block_hash != previous_header.block_hash:
            raise BitcoinInspectionError(
                f"header linkage breaks between heights {previous_header.height} and {current_header.height}"
            )


def _field_value(header: BitcoinHeader, field: str) -> int | str:
    if field not in SUPPORTED_FIELDS:
        raise ValueError(f"unsupported bitcoin header field: {field}")
    return getattr(header, field)


def _compress_header_runs(headers: list[BitcoinHeader], field: str) -> list[HeaderRun]:
    runs: list[HeaderRun] = []
    current_run: HeaderRun | None = None
    for header in headers:
        value = _field_value(header, field)
        if current_run and current_run.value == value:
            current_run = HeaderRun(
                value=current_run.value,
                start_height=current_run.start_height,
                end_height=header.height,
                start_block_hash=current_run.start_block_hash,
            )
            runs[-1] = current_run
            continue
        current_run = HeaderRun(
            value=value,
            start_height=header.height,
            end_height=header.height,
            start_block_hash=header.block_hash,
        )
        runs.append(current_run)
    return runs


def _occurrence_from_runs(first: HeaderRun, second: HeaderRun, third: HeaderRun, *, network: str, field: str) -> dict[str, Any]:
    payload = {
        "rule": PROFILE_ID,
        "network": network,
        "field": field,
        "occurrence_heights": [first.start_height, second.start_height, third.start_height],
        "block_hashes": [first.start_block_hash, second.start_block_hash, third.start_block_hash],
        "field_values": [first.value, second.value, third.value],
    }
    return {"id": _specimen_id(payload), **payload}


def _prospect_headers(headers: list[BitcoinHeader], *, network: str, field: str, start_height: int) -> dict[str, Any]:
    if field not in SUPPORTED_FIELDS:
        raise ValueError(f"unsupported bitcoin header field: {field}")
    runs = _compress_header_runs(headers, field)
    occurrences: list[dict[str, Any]] = []
    for index in range(len(runs) - 2):
        first, second, third = runs[index : index + 3]
        if first.value == third.value and first.value != second.value:
            occurrences.append(_occurrence_from_runs(first, second, third, network=network, field=field))
    return {
        "formation_rule": PROFILE_ID,
        "formation_summary": PROFILE_SUMMARY,
        "network": network,
        "field": field,
        "start_height": start_height,
        "end_height": start_height + len(headers) - 1 if headers else start_height - 1,
        "header_count": len(headers),
        "first_block_hash": headers[0].block_hash if headers else None,
        "last_block_hash": headers[-1].block_hash if headers else None,
        "occurrence_count": len(occurrences),
        "occurrences": occurrences,
    }


def prospect_bitcoin_occurrences(
    headers_file: str | Path,
    *,
    network: str,
    field: str,
    start_height: int = 0,
) -> dict[str, Any]:
    headers = read_block_headers(headers_file, start_height=start_height)
    return _prospect_headers(headers, network=network, field=field, start_height=start_height)


def export_bitcoin_evidence_bundle(prospect_result: dict[str, Any], occurrence: dict[str, Any]) -> dict[str, Any]:
    return export_evidence_bundle(
        prospect_result,
        occurrence,
        formation_rule={
            "id": PROFILE_ID,
            "summary": PROFILE_SUMMARY,
            "version": 1,
        },
        declared_source={
            "kind": "bitcoin-header-stream",
            "network": prospect_result["network"],
            "field": prospect_result["field"],
            "header_encoding": HEADER_ENCODING,
            "start_height": prospect_result["start_height"],
            "end_height": prospect_result["end_height"],
            "header_count": prospect_result["header_count"],
            "first_block_hash": prospect_result["first_block_hash"],
            "last_block_hash": prospect_result["last_block_hash"],
        },
        declared_coverage={
            "ordering": "in-file contiguous Bitcoin block-header order",
            "field_projection": prospect_result["field"],
            "run_compression": True,
            "broken_stream_behavior": "assay rejects malformed linkage; prospecting requires a contiguous header stream",
        },
    )


def _validate_bundle_shape(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if bundle.get("evidence_version") != EVIDENCE_VERSION:
        errors.append("unsupported evidence version")
    specimen = bundle.get("specimen")
    if not isinstance(specimen, dict):
        errors.append("missing specimen")
        return errors
    required_fields = ["id", "rule", "network", "field", "occurrence_heights", "block_hashes", "field_values"]
    for field_name in required_fields:
        if field_name not in specimen:
            errors.append(f"missing specimen field: {field_name}")
    return errors


def run_bitcoin_assay(headers_file: str | Path, bundle: dict[str, Any]) -> dict[str, Any]:
    errors = _validate_bundle_shape(bundle)
    if errors:
        return {"status": ASSAY_CONTRADICTED, "reasons": errors}

    integrity = (bundle.get("integrity") or {}).get("canonical_bundle_sha256")
    if not integrity:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["missing evidence integrity digest"]}
    if integrity != _bundle_integrity_sha256(bundle):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["evidence integrity digest mismatch"]}

    specimen = bundle["specimen"]
    if specimen.get("rule") != PROFILE_ID:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["unsupported formation rule"]}
    if len(specimen.get("occurrence_heights", [])) != 3 or len(specimen.get("block_hashes", [])) != 3:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["specimen must bind exactly three occurrence heights and three block hashes"]}
    if len(specimen.get("field_values", [])) != 3:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["specimen must bind exactly three field values"]}

    declared_source = bundle.get("declared_source") or {}
    network = declared_source.get("network")
    field = declared_source.get("field")
    start_height = declared_source.get("start_height")
    end_height = declared_source.get("end_height")
    header_count = declared_source.get("header_count")
    if network != specimen.get("network"):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["declared source network does not match specimen network"]}
    if field != specimen.get("field"):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["declared source field does not match specimen field"]}
    if not isinstance(start_height, int) or start_height < 0:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["missing or invalid start height in declared source"]}
    if not isinstance(header_count, int) or header_count < 0:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["missing or invalid header count in declared source"]}
    if header_count == 0:
        if end_height != start_height - 1:
            return {"status": ASSAY_CONTRADICTED, "reasons": ["declared empty header scope has an invalid height range"]}
    else:
        if not isinstance(end_height, int) or end_height < start_height:
            return {"status": ASSAY_CONTRADICTED, "reasons": ["missing or invalid end height in declared source"]}
        if end_height != start_height + header_count - 1:
            return {"status": ASSAY_CONTRADICTED, "reasons": ["declared source header count does not match the height range"]}

    try:
        headers = read_block_headers(headers_file, start_height=start_height)
    except (BitcoinInspectionError, OSError) as error:
        return {"status": ASSAY_INSUFFICIENT_EVIDENCE, "reasons": [str(error)]}
    except ValueError as error:
        return {"status": ASSAY_CONTRADICTED, "reasons": [str(error)]}

    if len(headers) != header_count:
        return {"status": ASSAY_INSUFFICIENT_EVIDENCE, "reasons": ["header stream does not contain the declared number of headers"]}
    if headers:
        if declared_source.get("first_block_hash") and headers[0].block_hash != declared_source["first_block_hash"]:
            return {"status": ASSAY_CONTRADICTED, "reasons": ["declared first block hash does not match the header stream"]}
        if declared_source.get("last_block_hash") and headers[-1].block_hash != declared_source["last_block_hash"]:
            return {"status": ASSAY_CONTRADICTED, "reasons": ["declared last block hash does not match the header stream"]}

    ordered_heights = specimen["occurrence_heights"]
    if any(previous_height >= next_height for previous_height, next_height in zip(ordered_heights, ordered_heights[1:])):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["occurrence heights must be strictly increasing in discovery order"]}

    for height, block_hash, field_value in zip(
        specimen["occurrence_heights"], specimen["block_hashes"], specimen["field_values"]
    ):
        if not isinstance(height, int):
            return {"status": ASSAY_CONTRADICTED, "reasons": ["occurrence heights must be integers"]}
        header_index = height - start_height
        if header_index < 0 or header_index >= len(headers):
            return {"status": ASSAY_CONTRADICTED, "reasons": [f"declared occurrence height is outside the assayed scope: {height}"]}
        header = headers[header_index]
        if header.block_hash != block_hash:
            return {"status": ASSAY_CONTRADICTED, "reasons": [f"declared block hash does not match height binding: {height}"]}
        if _field_value(header, field) != field_value:
            return {"status": ASSAY_CONTRADICTED, "reasons": [f"declared field value does not match height binding: {height}"]}

    prospect_result = _prospect_headers(headers, network=network, field=field, start_height=start_height)
    for occurrence in prospect_result["occurrences"]:
        if occurrence["id"] == specimen["id"]:
            if occurrence == specimen:
                return {
                    "status": ASSAY_VERIFIED,
                    "reasons": ["occurrence matches the declared Bitcoin header scope and recomputed evidence"],
                    "specimen": occurrence,
                }
            return {"status": ASSAY_CONTRADICTED, "reasons": ["specimen fields do not match recomputed occurrence"]}
    return {"status": ASSAY_CONTRADICTED, "reasons": ["occurrence not found within the declared Bitcoin header scope"]}
