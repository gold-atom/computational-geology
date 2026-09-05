from __future__ import annotations

import copy
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from computational_geology.engine import (
    ASSAY_CONTRADICTED,
    ASSAY_INSUFFICIENT_EVIDENCE,
    ASSAY_VERIFIED,
    catalogue_occurrences,
    export_evidence_bundle,
    prospect_occurrences,
    render_catalogue_html,
    run_assay,
)


class SyntheticGitFixture:
    def __init__(self, root: Path) -> None:
        self.repo = root / "fixture"
        self.repo.mkdir(parents=True, exist_ok=True)
        self.path = "strata/specimen.txt"
        self._git("init", "--initial-branch=main")
        self._git("config", "user.name", "Synthetic Fixture")
        self._git("config", "user.email", "synthetic@example.invalid")
        self.commit_index = 0

    def _git(self, *args: str, env: dict[str, str] | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
        merged_env = os.environ.copy()
        if env:
            merged_env.update(env)
        return subprocess.run(
            ["git", "-C", str(self.repo), *args],
            check=check,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=merged_env,
        )

    def commit_state(self, content: str | None, message: str) -> str:
        self.commit_index += 1
        timestamp = f"2001-01-{self.commit_index:02d}T00:00:00+0000"
        file_path = self.repo / self.path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if content is None:
            if file_path.exists():
                file_path.unlink()
            self._git("rm", "-f", "--ignore-unmatch", "--", self.path)
        else:
            file_path.write_text(content, encoding="utf-8")
            self._git("add", "--", self.path)
        env = {"GIT_AUTHOR_DATE": timestamp, "GIT_COMMITTER_DATE": timestamp}
        self._git("commit", "--allow-empty", "-m", message, env=env)
        return self.head()

    def head(self) -> str:
        return self._git("rev-parse", "HEAD").stdout.strip()


class EngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(prefix="computational-geology-tests-")
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def _fixture_with_states(self, states: list[str | None]) -> SyntheticGitFixture:
        fixture = SyntheticGitFixture(self.root)
        for index, state in enumerate(states, start=1):
            fixture.commit_state(state, f"state-{index}")
        return fixture

    def _bundle_from_fixture(self, fixture: SyntheticGitFixture) -> tuple[dict, dict]:
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertTrue(result["occurrences"])
        occurrence = result["occurrences"][0]
        return result, export_evidence_bundle(result, occurrence)

    def test_aba_yields_one_specimen(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(result["occurrence_count"], 1)

    def test_repeated_states_compress_to_same_pattern(self) -> None:
        fixture = self._fixture_with_states(["A\n", "A\n", "B\n", "B\n", "A\n"])
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(result["occurrence_count"], 1)

    def test_abc_does_not_yield_specimen(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "C\n"])
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(result["occurrence_count"], 0)

    def test_abca_does_not_qualify(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "C\n", "A\n"])
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(result["occurrence_count"], 0)

    def test_deletion_breaks_sequence(self) -> None:
        fixture = self._fixture_with_states(["A\n", None, "B\n", "A\n"])
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(result["occurrence_count"], 0)

    def test_rerunning_discovery_preserves_ids(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        first = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        second = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(first["occurrences"], second["occurrences"])

    def test_mirroring_history_preserves_ids(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        mirror = self.root / "mirror.git"
        subprocess.run(["git", "clone", "--mirror", str(fixture.repo), str(mirror)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        original = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        mirrored = prospect_occurrences(mirror, fixture.head(), fixture.path)
        self.assertEqual(original["occurrences"], mirrored["occurrences"])

    def test_appending_later_commits_preserves_earlier_ids(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        before = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        first_id = before["occurrences"][0]["id"]
        fixture.commit_state("A\n", "state-4")
        fixture.commit_state("D\n", "state-5")
        after = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertIn(first_id, [occurrence["id"] for occurrence in after["occurrences"]])

    def test_distinct_triples_receive_distinct_ids(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n", "C\n", "A\n"])
        result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        self.assertEqual(result["occurrence_count"], 2)
        ids = {occurrence["id"] for occurrence in result["occurrences"]}
        self.assertEqual(len(ids), 2)

    def test_altered_evidence_is_rejected(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        _, bundle = self._bundle_from_fixture(fixture)
        tampered = copy.deepcopy(bundle)
        tampered["specimen"]["blob_ids"][1] = tampered["specimen"]["blob_ids"][0]
        result = run_assay(fixture.repo, tampered)
        self.assertEqual(result["status"], ASSAY_CONTRADICTED)

    def test_missing_ancestry_is_insufficient_evidence(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        _, bundle = self._bundle_from_fixture(fixture)
        shallow = self.root / "shallow"
        subprocess.run(
            ["git", "clone", "--depth", "1", f"file://{fixture.repo}", str(shallow)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        result = run_assay(shallow, bundle)
        self.assertEqual(result["status"], ASSAY_INSUFFICIENT_EVIDENCE)

    def test_forged_verified_field_is_not_trusted(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        _, bundle = self._bundle_from_fixture(fixture)
        forged = copy.deepcopy(bundle)
        forged["verified"] = True
        forged["specimen"]["id"] = "forged"
        result = run_assay(fixture.repo, forged)
        self.assertEqual(result["status"], ASSAY_CONTRADICTED)

    def test_valid_assay_verifies_against_declared_scope(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        _, bundle = self._bundle_from_fixture(fixture)
        result = run_assay(fixture.repo, bundle)
        self.assertEqual(result["status"], ASSAY_VERIFIED)

    def test_catalogue_html_escapes_dynamic_values(self) -> None:
        specimen = {
            "id": '<script>alert(1)</script>',
            "path": 'strata/<layer>.txt',
            "occurrence_commits": ['a"', 'b&', 'c<'],
        }
        html_output = render_catalogue_html([specimen], {'<script>alert(1)</script>': ' 	javascript:alert(1)'})
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', html_output)
        self.assertIn('strata/&lt;layer&gt;.txt', html_output)
        self.assertNotIn('<script>alert(1)</script>', html_output)
        self.assertNotIn('href="javascript:alert(1)"', html_output)

    def test_parent_directory_segments_are_rejected(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        with self.assertRaisesRegex(ValueError, 'parent-directory'):
            prospect_occurrences(fixture.repo, fixture.head(), '../outside.txt')


    def test_catalogue_deduplicates_repeat_discoveries(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        prospect_result = prospect_occurrences(fixture.repo, fixture.head(), fixture.path)
        occurrence = prospect_result["occurrences"][0]
        bundle = export_evidence_bundle(prospect_result, occurrence)
        specimens = catalogue_occurrences([bundle, json.loads(json.dumps(bundle))])
        self.assertEqual(len(specimens), 1)

    def test_prospecting_leaves_repository_unchanged(self) -> None:
        fixture = self._fixture_with_states(["A\n", "B\n", "A\n"])
        config_before = (fixture.repo / ".git" / "config").read_text(encoding="utf-8")
        refs_before = fixture._git("show-ref").stdout
        status_before = fixture._git("status", "--porcelain=v1", "--untracked-files=all").stdout
        head_before = fixture.head()
        index_before = (fixture.repo / ".git" / "index").read_bytes()

        prospect_occurrences(fixture.repo, fixture.head(), fixture.path)

        self.assertEqual((fixture.repo / ".git" / "config").read_text(encoding="utf-8"), config_before)
        self.assertEqual(fixture._git("show-ref").stdout, refs_before)
        self.assertEqual(fixture._git("status", "--porcelain=v1", "--untracked-files=all").stdout, status_before)
        self.assertEqual(fixture.head(), head_before)
        self.assertEqual((fixture.repo / ".git" / "index").read_bytes(), index_before)


if __name__ == "__main__":
    unittest.main()
