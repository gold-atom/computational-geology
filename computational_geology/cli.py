from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path

from .engine import (
    ASSAY_CONTRADICTED,
    ASSAY_VERIFIED,
    catalogue_occurrences,
    export_evidence_bundle,
    prospect_occurrences,
    render_catalogue_html,
    run_assay,
)


def _write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _cmd_prospect(args: argparse.Namespace) -> int:
    result = prospect_occurrences(args.repo, args.commit, args.path)
    if args.evidence_dir:
        evidence_dir = Path(args.evidence_dir)
        for occurrence in result["occurrences"]:
            bundle = export_evidence_bundle(result, occurrence)
            _write_json(evidence_dir / f"{occurrence['id']}.json", bundle)
    if args.output:
        _write_json(Path(args.output), result)
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def _cmd_assay(args: argparse.Namespace) -> int:
    result = run_assay(args.repo, _load_json(Path(args.evidence)))
    if args.output:
        _write_json(Path(args.output), result)
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] == ASSAY_CONTRADICTED:
        return 1
    if result["status"] != ASSAY_VERIFIED:
        return 2
    return 0


def _cmd_catalogue(args: argparse.Namespace) -> int:
    evidence_paths = [Path(path) for path in args.evidence_files]
    bundles = [_load_json(path) for path in evidence_paths]
    specimens = catalogue_occurrences(bundles)
    links: dict[str, str] = {}
    for bundle, path in zip(bundles, evidence_paths):
        specimen_id = bundle.get("specimen", {}).get("id")
        if specimen_id and specimen_id not in links:
            links[specimen_id] = path.name
    html = render_catalogue_html(specimens, links)
    output_path = Path(args.output_html)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    return 0


def _git(repository: Path, *args: str, env: dict[str, str] | None = None) -> None:
    import os
    import subprocess

    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    subprocess.run(["git", "-C", str(repository), *args], check=True, env=merged_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def _build_synthetic_fixture(root: Path) -> tuple[Path, str, str]:
    repo = root / "synthetic-repo"
    repo.mkdir(parents=True, exist_ok=True)
    _git(repo, "init", "--initial-branch=main")
    _git(repo, "config", "user.name", "Synthetic Fixture")
    _git(repo, "config", "user.email", "synthetic@example.invalid")
    path = "strata/specimen.txt"
    file_path = repo / path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    states = [
        ("A", "layer one\n", "2001-01-01T00:00:00+0000"),
        ("B", "layer two\n", "2001-01-02T00:00:00+0000"),
        ("A return", "layer one\n", "2001-01-03T00:00:00+0000"),
    ]
    pinned_commit = ""
    for message, content, timestamp in states:
        file_path.write_text(content, encoding="utf-8")
        _git(repo, "add", "--", path)
        commit_env = {"GIT_AUTHOR_DATE": timestamp, "GIT_COMMITTER_DATE": timestamp}
        _git(repo, "commit", "-m", message, env=commit_env)
    import subprocess

    pinned_commit = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, stdout=subprocess.PIPE, text=True
    ).stdout.strip()
    return repo, pinned_commit, path


def _cmd_demo(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="computational-geology-demo-") as temp_dir:
        repo, pinned_commit, path = _build_synthetic_fixture(Path(temp_dir))
        prospect_result = prospect_occurrences(repo, pinned_commit, path)
        _write_json(output_dir / "prospect.json", prospect_result)
        if not prospect_result["occurrences"]:
            raise SystemExit("synthetic fixture did not produce an occurrence")
        bundle = export_evidence_bundle(prospect_result, prospect_result["occurrences"][0])
        valid_evidence = output_dir / "valid-specimen.json"
        _write_json(valid_evidence, bundle)
        valid_assay = run_assay(repo, bundle)
        _write_json(output_dir / "valid-assay.json", valid_assay)

        tampered_bundle = json.loads(json.dumps(bundle))
        tampered_bundle["verified"] = True
        tampered_bundle["specimen"]["blob_ids"][1] = tampered_bundle["specimen"]["blob_ids"][0]
        _write_json(output_dir / "tampered-specimen.json", tampered_bundle)
        tampered_assay = run_assay(repo, tampered_bundle)
        _write_json(output_dir / "tampered-assay.json", tampered_assay)

        specimens = catalogue_occurrences([bundle])
        html = render_catalogue_html(specimens, {bundle["specimen"]["id"]: valid_evidence.name})
        (output_dir / "catalogue.html").write_text(html, encoding="utf-8")

        print(f"Synthetic repository: {repo}")
        print(f"Pinned commit: {pinned_commit}")
        print(f"Valid assay: {valid_assay['status']}")
        print(f"Tampered assay: {tampered_assay['status']}")
        print(f"Catalogue: {output_dir / 'catalogue.html'}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="computational-geology")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prospect = subparsers.add_parser("prospect", help="Enumerate exact-content return occurrences.")
    prospect.add_argument("--repo", required=True)
    prospect.add_argument("--commit", required=True)
    prospect.add_argument("--path", required=True)
    prospect.add_argument("--output")
    prospect.add_argument("--evidence-dir")
    prospect.set_defaults(func=_cmd_prospect)

    assay = subparsers.add_parser("assay", help="Recompute and verify an evidence bundle.")
    assay.add_argument("--repo", required=True)
    assay.add_argument("--evidence", required=True)
    assay.add_argument("--output")
    assay.set_defaults(func=_cmd_assay)

    catalogue = subparsers.add_parser("catalogue", help="Deduplicate evidence bundles into a static HTML catalogue.")
    catalogue.add_argument("--output-html", required=True)
    catalogue.add_argument("evidence_files", nargs="+")
    catalogue.set_defaults(func=_cmd_catalogue)

    demo = subparsers.add_parser("demo", help="Create and verify a deterministic synthetic demonstration.")
    demo.add_argument("--output-dir", required=True)
    demo.set_defaults(func=_cmd_demo)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
