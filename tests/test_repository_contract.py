import hashlib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MEDIA = {
    "animations/01-portrait-markbuild-full-contact-25s.mp4": (
        8_286_219,
        "d0bb5232b30e8e1ecc57ff5229b1e5fd7a5746ce99d8d61da2fee447c4df040f",
    ),
    "animations/02-bathroom-svg-reveal-25s.mp4": (
        3_097_091,
        "a7bd0d91aface1ccf123401b1f10a253e24e26fa2b0d34811036c78268ba0676",
    ),
    "animations/03-fashion-markbuild-full-contact-25s.mp4": (
        9_713_253,
        "fe4c716b0d7dd629b10a35f9ab874ee78413bcdce91557263f13b97f27c19a24",
    ),
}


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class RepositoryContractTests(unittest.TestCase):
    def test_project_documentation_contract_exists(self) -> None:
        required = (
            "README.md",
            "PROJECT.md",
            "AGENTS.md",
            "CONTEXT.md",
            "context.toml",
            "docs/adr/0001-treat-mp4s-as-published-media-evidence.md",
            "docs/agents/domain.md",
            "docs/agents/issue-tracker.md",
            "docs/agents/triage-labels.md",
            ".github/workflows/validate.yml",
        )

        self.assertEqual(
            [path for path in required if not (ROOT / path).is_file()],
            [],
        )

    def test_readme_states_the_media_snapshot_boundary(self) -> None:
        text = read("README.md")

        self.assertIn("Published Media Snapshot", text)
        self.assertIn("does not contain the generating source", text)
        self.assertIn("Deployment ownership: none", text)
        self.assertIn("[PROJECT.md](PROJECT.md)", text)
        self.assertIn("[CONTEXT.md](CONTEXT.md)", text)

    def test_media_bytes_match_the_published_snapshot(self) -> None:
        for relative_path, (expected_size, expected_sha256) in MEDIA.items():
            path = ROOT / relative_path
            digest = hashlib.sha256()
            with path.open("rb") as handle:
                while chunk := handle.read(1024 * 1024):
                    digest.update(chunk)

            self.assertEqual(path.stat().st_size, expected_size, relative_path)
            self.assertEqual(digest.hexdigest(), expected_sha256, relative_path)
            self.assertEqual(path.read_bytes()[4:8], b"ftyp", relative_path)

    def test_project_packet_records_verified_media_and_unknown_provenance(self) -> None:
        text = read("PROJECT.md")

        self.assertIn("348af448e71d53ab94a4aa6b4b6d4ad8b2204057", text)
        self.assertIn("three silent 25-second", text)
        self.assertIn("1920x1080", text)
        self.assertIn("H.264", text)
        self.assertIn("generating source remains unresolved", text)
        self.assertIn("GitHub Pages is absent", text)
        self.assertIn("issues/1", text)
        self.assertIn("issues/2", text)
        self.assertIn("issues/3", text)

    def test_active_contracts_do_not_embed_private_machine_paths(self) -> None:
        private_home = "/" + "home/reidsurmeier"
        paths = (
            "README.md",
            "PROJECT.md",
            "AGENTS.md",
            "CONTEXT.md",
            "context.toml",
            ".github/workflows/validate.yml",
        )

        for relative_path in paths:
            self.assertNotIn(private_home, read(relative_path), relative_path)


if __name__ == "__main__":
    unittest.main()
