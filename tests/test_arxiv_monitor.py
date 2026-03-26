import json
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from pathlib import Path

sys.modules.setdefault("feedparser", types.SimpleNamespace(parse=lambda url: None))

from arxiv_monitor import ArxivMonitor


class ArxivMonitorSavePapersTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_dir = Path(self.temp_dir.name)
        self.config_path = self.repo_dir / "config.yaml"
        self.config_path.write_text(
            "\n".join(
                [
                    "arxiv:",
                    "  categories: []",
                    "  keywords:",
                    "    include: []",
                    "    exclude: []",
                    f"  seen_file: \"{self.repo_dir / '.seen_papers.json'}\"",
                    "github:",
                    "  branch: master",
                    "logging:",
                    "  level: INFO",
                ]
            ),
            encoding="utf-8",
        )
        self.monitor = ArxivMonitor(config_path=str(self.config_path))
        self.monitor.output_dir = self.repo_dir / "papers"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_papers_writes_base_json_without_rendering_readme(self):
        paper = {
            "id": "paper-1",
            "title": "Paper title",
            "authors": ["Alice", "Bob"],
            "summary": "English abstract",
            "published": "Wed, 25 Mar 2026 00:00:00 -0400",
            "link": "https://example.com/paper-1",
            "pdf": "https://example.com/paper-1.pdf",
            "category": "cs.SD",
            "fetched_at": "2026-03-26T00:00:00+00:00",
        }

        self.monitor.save_papers([paper], "2026-03-26")

        date_dir = self.monitor.output_dir / "2026-03-26"
        paper_path = date_dir / "paper-1.json"
        self.assertTrue(paper_path.exists())
        self.assertFalse((date_dir / "README.md").exists())

        stored = json.loads(paper_path.read_text(encoding="utf-8"))
        self.assertEqual(stored["pdf"], "https://example.com/paper-1.pdf")
        self.assertEqual(stored["fetched_at"], "2026-03-26T00:00:00+00:00")
        self.assertNotIn("summary_zh", stored)
        self.assertNotIn("title_zh", stored)

    def test_run_creates_empty_day_directory_when_no_papers(self):
        class FakeDateTime:
            @classmethod
            def now(cls):
                class FakeNow:
                    def strftime(self, fmt):
                        return "2026-03-27"

                return FakeNow()

        with patch.object(self.monitor, "fetch_all_papers", return_value=[]):
            with patch("arxiv_monitor.datetime.datetime", FakeDateTime):
                self.monitor.run()

        self.assertTrue((self.monitor.output_dir / "2026-03-27").exists())
        self.assertFalse((self.monitor.output_dir / "2026-03-27" / "README.md").exists())


if __name__ == "__main__":
    unittest.main()
