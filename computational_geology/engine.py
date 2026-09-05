from __future__ import annotations

import hashlib
import html
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlsplit

PROFILE_ID = "git-state-return/v1"
PROFILE_SUMMARY = (
    "Three consecutive first-parent runs for one repository-relative path with blob labels A->B->A, "
    "where A and B differ."
)
EVIDENCE_VERSION = "computational-geology-evidence/v1"
ASSAY_VERIFIED = "VERIFIED WITHIN DECLARED SCOPE"
ASSAY_CONTRADICTED = "CONTRADICTED"
ASSAY_INSUFFICIENT_EVIDENCE = "INSUFFICIENT EVIDENCE"
ORDINARY_FILE_MODES = {"100644", "100755"}


class GitInspectionError(RuntimeError):
    """Raised when the source repository cannot be inspected as declared."""


@dataclass(frozen=True)
class Run:
    blob_id: str
    start_commit: str
    end_commit: str


@dataclass(frozen=True)
class ProspectContext:
    repository: Path
    pinned_commit: str
    path: str
    git_object_hash: str
    commits: tuple[str, ...]
    ancestry_complete: bool
    missing_parent: str | None


def _canonical_json(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _run_git(repository: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    command = ["git", "-c", "safe.bareRepository=all", "-C", str(repository), *args]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if check and result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise GitInspectionError(stderr or f"git command failed: {' '.join(command)}")
    return result


def _known_evidence_payload(bundle: dict[str, Any]) -> dict[str, Any]:
    specimen = bundle.get("specimen") or {}
    return {
        "evidence_version": bundle.get("evidence_version"),
        "formation_rule": bundle.get("formation_rule"),
        "declared_source": bundle.get("declared_source"),
        "declared_coverage": bundle.get("declared_coverage"),
        "specimen": {
            "id": specimen.get("id"),
            "rule": specimen.get("rule"),
            "git_object_hash": specimen.get("git_object_hash"),
            "path": specimen.get("path"),
            "path_utf8_hex": specimen.get("path_utf8_hex"),
            "occurrence_commits": specimen.get("occurrence_commits"),
            "blob_ids": specimen.get("blob_ids"),
        },
        "external_witnesses": bundle.get("external_witnesses", []),
    }


def _bundle_integrity_sha256(bundle: dict[str, Any]) -> str:
    payload = _known_evidence_payload(bundle)
    return hashlib.sha256(b"computational-geology:evidence:v1\0" + _canonical_json(payload)).hexdigest()


def _specimen_payload(
    *, rule: str, git_object_hash: str, path: str, occurrence_commits: list[str], blob_ids: list[str]
) -> dict[str, Any]:
    return {
        "rule": rule,
        "git_object_hash": git_object_hash,
        "path": path,
        "path_utf8_hex": path.encode("utf-8").hex(),
        "occurrence_commits": occurrence_commits,
        "blob_ids": blob_ids,
    }


def _specimen_id(payload: dict[str, Any]) -> str:
    digest = hashlib.sha256(b"computational-geology:specimen:v1\0" + _canonical_json(payload)).hexdigest()
    return f"cg-specimen-v1-sha256:{digest}"


def _git_object_hash(repository: Path) -> str:
    return _run_git(repository, "rev-parse", "--show-object-format").stdout.decode("utf-8").strip()


def _first_parent(repository: Path, commit: str) -> str | None:
    commit_body = _run_git(repository, "cat-file", "-p", commit).stdout.decode("utf-8")
    for line in commit_body.splitlines():
        if line.startswith("parent "):
            return line.split()[1]
    return None


def _require_relative_path(path: str) -> None:
    pure_path = PurePosixPath(path)
    if not path or pure_path.is_absolute():
        raise ValueError("path must be a non-empty repository-relative path")
    if ".." in pure_path.parts:
        raise ValueError("path must not contain parent-directory segments")
    normalized = pure_path.as_posix()
    if normalized in {"", "."} or normalized != path:
        raise ValueError("path must use a normalized repository-relative form")


def _load_context(repository: str | Path, pinned_commit: str, path: str) -> ProspectContext:
    repo_path = Path(repository)
    _require_relative_path(path)
    commit_check = _run_git(repo_path, "cat-file", "-e", f"{pinned_commit}^{{commit}}", check=False)
    if commit_check.returncode != 0:
        raise GitInspectionError(f"missing pinned commit object: {pinned_commit}")

    walked_commits: list[str] = []
    current_commit = pinned_commit
    missing_parent = None
    ancestry_complete = True
    while True:
        walked_commits.append(current_commit)
        first_parent = _first_parent(repo_path, current_commit)
        if first_parent is None:
            break
        parent_check = _run_git(repo_path, "cat-file", "-e", f"{first_parent}^{{commit}}", check=False)
        if parent_check.returncode != 0:
            missing_parent = first_parent
            ancestry_complete = False
            break
        current_commit = first_parent

    commits = tuple(reversed(walked_commits))
    return ProspectContext(
        repository=repo_path,
        pinned_commit=pinned_commit,
        path=path,
        git_object_hash=_git_object_hash(repo_path),
        commits=commits,
        ancestry_complete=ancestry_complete,
        missing_parent=missing_parent,
    )


def _blob_at_path(repository: Path, commit: str, path: str) -> str | None:
    listing = _run_git(repository, "ls-tree", "-z", commit, "--", path).stdout
    if not listing:
        return None
    entry = listing.rstrip(b"\0").split(b"\0")[0]
    metadata, actual_path = entry.split(b"\t", 1)
    mode, object_type, object_id = metadata.decode("ascii").split(" ")
    if actual_path != path.encode("utf-8"):
        return None
    if object_type != "blob" or mode not in ORDINARY_FILE_MODES:
        return None
    return object_id


def _read_object_type(repository: Path, object_id: str) -> str | None:
    object_type = _run_git(repository, "cat-file", "-t", object_id, check=False)
    if object_type.returncode != 0:
        return None
    return object_type.stdout.decode("utf-8").strip()


def _read_object_bytes(repository: Path, object_type: str, object_id: str) -> bytes | None:
    object_data = _run_git(repository, "cat-file", object_type, object_id, check=False)
    if object_data.returncode != 0:
        return None
    return object_data.stdout


def _object_id_for_bytes(object_type: str, content: bytes, hash_name: str) -> str:
    digest = hashlib.new(hash_name)
    digest.update(f"{object_type} {len(content)}\0".encode("ascii"))
    digest.update(content)
    return digest.hexdigest()


def _compress_run_segments(context: ProspectContext) -> list[list[Run]]:
    segments: list[list[Run]] = []
    current_segment: list[Run] = []
    current_run: Run | None = None
    for commit in context.commits:
        blob_id = _blob_at_path(context.repository, commit, context.path)
        if blob_id is None:
            current_run = None
            if current_segment:
                segments.append(current_segment)
                current_segment = []
            continue
        if current_run and current_run.blob_id == blob_id:
            current_run = Run(blob_id=blob_id, start_commit=current_run.start_commit, end_commit=commit)
            current_segment[-1] = current_run
            continue
        current_run = Run(blob_id=blob_id, start_commit=commit, end_commit=commit)
        current_segment.append(current_run)
    if current_segment:
        segments.append(current_segment)
    return segments


def _occurrence_from_runs(context: ProspectContext, first: Run, second: Run, third: Run) -> dict[str, Any]:
    blob_ids = [first.blob_id, second.blob_id, third.blob_id]
    occurrence_commits = [first.start_commit, second.start_commit, third.start_commit]
    payload = _specimen_payload(
        rule=PROFILE_ID,
        git_object_hash=context.git_object_hash,
        path=context.path,
        occurrence_commits=occurrence_commits,
        blob_ids=blob_ids,
    )
    return {"id": _specimen_id(payload), **payload}


def prospect_occurrences(repository: str | Path, pinned_commit: str, path: str) -> dict[str, Any]:
    context = _load_context(repository, pinned_commit, path)
    segments = _compress_run_segments(context)
    occurrences: list[dict[str, Any]] = []
    for runs in segments:
        for index in range(len(runs) - 2):
            first, second, third = runs[index : index + 3]
            if first.blob_id == third.blob_id and first.blob_id != second.blob_id:
                occurrences.append(_occurrence_from_runs(context, first, second, third))
    return {
        "formation_rule": PROFILE_ID,
        "formation_summary": PROFILE_SUMMARY,
        "git_object_hash": context.git_object_hash,
        "pinned_commit": context.pinned_commit,
        "path": context.path,
        "ancestry_complete": context.ancestry_complete,
        "missing_parent": context.missing_parent,
        "occurrence_count": len(occurrences),
        "occurrences": occurrences,
    }


def export_evidence_bundle(prospect_result: dict[str, Any], occurrence: dict[str, Any]) -> dict[str, Any]:
    bundle = {
        "evidence_version": EVIDENCE_VERSION,
        "formation_rule": {
            "id": PROFILE_ID,
            "summary": PROFILE_SUMMARY,
            "version": 1,
        },
        "declared_source": {
            "kind": "git-local-repository",
            "pinned_commit": prospect_result["pinned_commit"],
            "first_parent_only": True,
            "path": prospect_result["path"],
        },
        "declared_coverage": {
            "ancestry_order": "oldest-to-newest first-parent ancestry ending at the pinned commit",
            "path_match": "exact repository-relative path",
            "ordinary_file_modes": sorted(ORDINARY_FILE_MODES),
            "rename_heuristics": False,
            "second_parents": False,
            "missing_path_breaks_sequence": True,
            "unsupported_entry_breaks_sequence": True,
        },
        "specimen": occurrence,
        "external_witnesses": [],
    }
    bundle["integrity"] = {"canonical_bundle_sha256": _bundle_integrity_sha256(bundle)}
    return bundle


def _validate_bundle_shape(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if bundle.get("evidence_version") != EVIDENCE_VERSION:
        errors.append("unsupported evidence version")
    specimen = bundle.get("specimen")
    if not isinstance(specimen, dict):
        errors.append("missing specimen")
        return errors
    required_specimen_fields = ["id", "rule", "git_object_hash", "path", "path_utf8_hex", "occurrence_commits", "blob_ids"]
    for field_name in required_specimen_fields:
        if field_name not in specimen:
            errors.append(f"missing specimen field: {field_name}")
    return errors


def run_assay(repository: str | Path, bundle: dict[str, Any]) -> dict[str, Any]:
    repository_path = Path(repository)
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
    payload = _specimen_payload(
        rule=specimen["rule"],
        git_object_hash=specimen["git_object_hash"],
        path=specimen["path"],
        occurrence_commits=list(specimen["occurrence_commits"]),
        blob_ids=list(specimen["blob_ids"]),
    )
    if len(specimen.get("occurrence_commits", [])) != 3 or len(specimen.get("blob_ids", [])) != 3:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["specimen must bind exactly three occurrence commits and three blob identities"]}
    if specimen.get("path_utf8_hex") != payload["path_utf8_hex"]:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["path encoding mismatch"]}
    if specimen.get("id") != _specimen_id(payload):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["specimen identifier mismatch"]}

    declared_source = bundle.get("declared_source") or {}
    pinned_commit = declared_source.get("pinned_commit")
    path = declared_source.get("path")
    if not pinned_commit:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["missing pinned commit in declared source"]}
    if not path:
        return {"status": ASSAY_CONTRADICTED, "reasons": ["missing path in declared source"]}
    if path != specimen.get("path"):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["declared source path does not match specimen path"]}

    try:
        prospect_result = prospect_occurrences(repository_path, pinned_commit, path)
    except GitInspectionError as error:
        return {"status": ASSAY_INSUFFICIENT_EVIDENCE, "reasons": [str(error)]}
    except ValueError as error:
        return {"status": ASSAY_CONTRADICTED, "reasons": [str(error)]}

    if prospect_result["git_object_hash"] != specimen.get("git_object_hash"):
        return {"status": ASSAY_CONTRADICTED, "reasons": ["git object hash algorithm mismatch"]}
    if not prospect_result["ancestry_complete"]:
        reason = "first-parent ancestry is incomplete"
        if prospect_result.get("missing_parent"):
            reason = f"missing first-parent commit object: {prospect_result['missing_parent']}"
        return {"status": ASSAY_INSUFFICIENT_EVIDENCE, "reasons": [reason]}
    for occurrence_commit, blob_id in zip(specimen["occurrence_commits"], specimen["blob_ids"]):
        commit_check = _run_git(repository_path, "cat-file", "-e", f"{occurrence_commit}^{{commit}}", check=False)
        if commit_check.returncode != 0:
            return {
                "status": ASSAY_INSUFFICIENT_EVIDENCE,
                "reasons": [f"missing required occurrence commit object: {occurrence_commit}"],
            }
        observed_blob_id = _blob_at_path(repository_path, occurrence_commit, path)
        if observed_blob_id is None:
            return {
                "status": ASSAY_CONTRADICTED,
                "reasons": [f"declared occurrence does not bind an ordinary file blob: {occurrence_commit} {path}"],
            }
        if observed_blob_id != blob_id:
            return {
                "status": ASSAY_CONTRADICTED,
                "reasons": [f"declared blob does not match commit/path binding: {occurrence_commit}"],
            }
    for blob_id in dict.fromkeys(specimen["blob_ids"]):
        object_type = _read_object_type(repository_path, blob_id)
        if object_type is None:
            return {"status": ASSAY_INSUFFICIENT_EVIDENCE, "reasons": [f"missing required blob object: {blob_id}"]}
        if object_type != "blob":
            return {"status": ASSAY_CONTRADICTED, "reasons": [f"required object is not a blob: {blob_id} ({object_type})"]}
        object_bytes = _read_object_bytes(repository_path, object_type, blob_id)
        if object_bytes is None:
            return {"status": ASSAY_INSUFFICIENT_EVIDENCE, "reasons": [f"missing required blob bytes: {blob_id}"]}
        if _object_id_for_bytes(object_type, object_bytes, prospect_result["git_object_hash"]) != blob_id:
            return {
                "status": ASSAY_CONTRADICTED,
                "reasons": [f"required blob bytes do not match object identity: {blob_id}"],
            }

    for occurrence in prospect_result["occurrences"]:
        if occurrence["id"] == specimen["id"]:
            if occurrence == specimen:
                return {
                    "status": ASSAY_VERIFIED,
                    "reasons": ["occurrence matches the declared source scope and recomputed evidence"],
                    "specimen": occurrence,
                }
            return {"status": ASSAY_CONTRADICTED, "reasons": ["specimen fields do not match recomputed occurrence"]}
    return {"status": ASSAY_CONTRADICTED, "reasons": ["occurrence not found within the declared source scope"]}


def catalogue_occurrences(bundles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    catalogue: dict[str, dict[str, Any]] = {}
    bundle_signatures: dict[str, bytes] = {}
    required_fields = {"id", "path", "occurrence_commits"}
    for bundle in bundles:
        specimen = bundle.get("specimen") or {}
        specimen_id = specimen.get("id")
        if not specimen_id:
            continue
        missing_fields = sorted(field_name for field_name in required_fields if field_name not in specimen)
        if missing_fields:
            raise ValueError(f"malformed catalogue specimen {specimen_id}: missing {', '.join(missing_fields)}")
        if len(specimen.get("occurrence_commits", [])) != 3:
            raise ValueError(f"malformed catalogue specimen {specimen_id}: expected three occurrence commits")
        signature = _canonical_json({
            "payload": _known_evidence_payload(bundle),
            "integrity": (bundle.get("integrity") or {}).get("canonical_bundle_sha256"),
        })
        if specimen_id in bundle_signatures and bundle_signatures[specimen_id] != signature:
            raise ValueError(f"conflicting specimen evidence for {specimen_id}")
        bundle_signatures.setdefault(specimen_id, signature)
        catalogue.setdefault(specimen_id, specimen)
    return [catalogue[specimen_id] for specimen_id in sorted(catalogue)]


def _safe_catalogue_href(href: str) -> str | None:
    if not href or href != href.strip(" \t\r\n\f\v"):
        return None
    if any(ord(character) < 32 or ord(character) == 127 for character in href):
        return None
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        return None
    pure_path = PurePosixPath(parsed.path)
    if pure_path.is_absolute() or ".." in pure_path.parts:
        return None
    normalized = pure_path.as_posix()
    if normalized in {"", "."} or normalized != parsed.path:
        return None
    suffix = ""
    if parsed.query:
        suffix += f"?{parsed.query}"
    if parsed.fragment:
        suffix += f"#{parsed.fragment}"
    return normalized + suffix


def render_catalogue_html(specimens: list[dict[str, Any]], evidence_links: dict[str, str] | None = None) -> str:
    evidence_links = evidence_links or {}
    lines = [
        "<!doctype html>",
        "<html lang=\"en\">",
        "<head>",
        "  <meta charset=\"utf-8\">",
        "  <title>Computational Geology Catalogue</title>",
        "</head>",
        "<body>",
        "  <h1>SYNTHETIC FIXTURE</h1>",
        "  <p>This catalogue was generated from a deterministic synthetic fixture. It is not an independently witnessed historical discovery.</p>",
        "  <ul>",
    ]
    for specimen in specimens:
        evidence_link = evidence_links.get(specimen["id"])
        safe_href = _safe_catalogue_href(evidence_link) if evidence_link else None
        identifier = html.escape(specimen["id"], quote=True)
        description = html.escape(
            f"{specimen['path']} :: {' → '.join(specimen['occurrence_commits'])}", quote=True
        )
        if safe_href:
            href = html.escape(safe_href, quote=True)
            lines.append(f"    <li><a href=\"{href}\">{identifier}</a><br>{description}</li>")
        else:
            lines.append(f"    <li>{identifier}<br>{description}</li>")
    lines.extend(["  </ul>", "</body>", "</html>"])
    return "\n".join(lines) + "\n"
