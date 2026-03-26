import json
import tempfile
import unittest
from pathlib import Path

import render_daily


class RenderDailyTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_dir = Path(self.temp_dir.name)
        self.base_dir = self.repo_dir / "papers"
        self.base_dir.mkdir()
        self.root_readme = self.repo_dir / "README.md"

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_day(self, date_str, papers):
        date_dir = self.base_dir / date_str
        date_dir.mkdir(parents=True)
        for index, paper in enumerate(papers, start=1):
            path = date_dir / f"paper-{index}.json"
            path.write_text(json.dumps(paper, ensure_ascii=False), encoding="utf-8")
        return date_dir

    def test_render_all_prefers_summary_zh_and_fallback(self):
        self.make_day(
            "2026-03-26",
            [
                {
                    "id": "paper-1",
                    "title": "Paper One",
                    "authors": "Alice, Bob",
                    "summary": "English abstract one",
                    "summary_zh": "中文摘要一",
                    "published": "Wed, 25 Mar 2026 00:00:00 -0400",
                    "link": "https://example.com/1",
                    "pdf": "https://example.com/1.pdf",
                    "category": "cs.SD",
                },
                {
                    "id": "paper-2",
                    "title": "Paper Two",
                    "authors": ["Carol"],
                    "summary": "English abstract two",
                    "published": "Wed, 25 Mar 2026 00:00:00 -0400",
                    "link": "https://example.com/2",
                    "pdf": "https://example.com/2.pdf",
                    "category": "eess.AS",
                },
            ],
        )

        render_daily.render_all(
            "2026-03-26",
            base_dir=self.base_dir,
            root_readme=self.root_readme,
        )

        readme = (self.base_dir / "2026-03-26" / "README.md").read_text(encoding="utf-8")
        self.assertIn("中文摘要一", readme)
        self.assertNotIn("English abstract one", readme)
        self.assertIn("中文摘要翻译失败，请查看原文 JSON。", readme)

    def test_render_all_updates_root_readme_and_latest_symlink(self):
        self.make_day(
            "2026-03-25",
            [
                {
                    "id": "older-paper",
                    "title": "Older",
                    "authors": "Alice",
                    "summary": "Older abstract",
                    "published": "Tue, 24 Mar 2026 00:00:00 -0400",
                    "link": "https://example.com/older",
                    "pdf": "https://example.com/older.pdf",
                    "category": "cs.SD",
                }
            ],
        )
        self.make_day(
            "2026-03-26",
            [
                {
                    "id": "new-paper",
                    "title": "New",
                    "authors": "Bob",
                    "summary": "New abstract",
                    "summary_zh": "新的中文摘要",
                    "published": "Wed, 25 Mar 2026 00:00:00 -0400",
                    "link": "https://example.com/new",
                    "pdf": "https://example.com/new.pdf",
                    "category": "cs.SD",
                }
            ],
        )

        render_daily.render_all(
            "2026-03-26",
            base_dir=self.base_dir,
            root_readme=self.root_readme,
        )

        root = self.root_readme.read_text(encoding="utf-8")
        self.assertIn("2026-03-26", root)
        self.assertIn("[1 papers](papers/latest/)", root)

        latest = self.base_dir / "latest"
        self.assertTrue(latest.is_symlink())
        self.assertEqual(latest.resolve(), (self.base_dir / "2026-03-26").resolve())


if __name__ == "__main__":
    unittest.main()
