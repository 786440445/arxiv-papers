import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

import translate_papers


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def read(self):
        return json.dumps(self.payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class TranslatePapersTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name) / "papers"
        self.date_dir = self.base_dir / "2026-03-26"
        self.date_dir.mkdir(parents=True)

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_paper(self, filename, title, summary):
        paper = {
            "id": filename.replace(".json", ""),
            "title": title,
            "summary": summary,
            "link": f"https://example.com/{filename}",
        }
        path = self.date_dir / filename
        path.write_text(json.dumps(paper, ensure_ascii=False), encoding="utf-8")
        return path

    def read_paper(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_translate_date_papers_writes_summary_zh_and_metadata(self):
        paper_path = self.write_paper("paper-a.json", "Test title", "Original abstract")
        requests_seen = []

        def fake_urlopen(request, timeout=0):
            requests_seen.append((request, timeout))
            return FakeResponse(
                {
                    "choices": [
                        {
                            "message": {
                                "content": "中文摘要内容"
                            }
                        }
                    ]
                }
            )

        with patch("translate_papers.urlopen", side_effect=fake_urlopen, create=True):
            translate_papers.translate_date_papers(
                "2026-03-26",
                base_dir=self.base_dir,
                api_key="test-key",
            )

        updated = self.read_paper(paper_path)
        self.assertEqual(updated["summary_zh"], "中文摘要内容")
        self.assertEqual(updated["translation_model"], "stepfun/step-3.5-flash:free")
        self.assertIn("translation_updated_at", updated)
        self.assertEqual(len(requests_seen), 1)

        request, timeout = requests_seen[0]
        self.assertEqual(timeout, 120)
        payload = json.loads(request.data.decode("utf-8"))
        self.assertEqual(payload["model"], "stepfun/step-3.5-flash:free")

    def test_translate_date_papers_skips_failed_item_and_continues(self):
        first_path = self.write_paper("paper-a.json", "First title", "First abstract")
        second_path = self.write_paper("paper-b.json", "Second title", "Second abstract")
        call_count = {"value": 0}

        def fake_urlopen(request, timeout=0):
            call_count["value"] += 1
            if call_count["value"] == 1:
                raise HTTPError(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    code=429,
                    msg="rate limited",
                    hdrs=None,
                    fp=None,
                )
            return FakeResponse(
                {
                    "choices": [
                        {
                            "message": {
                                "content": "第二篇中文摘要"
                            }
                        }
                    ]
                }
            )

        with patch("translate_papers.urlopen", side_effect=fake_urlopen, create=True):
            translate_papers.translate_date_papers(
                "2026-03-26",
                base_dir=self.base_dir,
                api_key="test-key",
            )

        first = self.read_paper(first_path)
        second = self.read_paper(second_path)
        self.assertNotIn("summary_zh", first)
        self.assertEqual(second["summary_zh"], "第二篇中文摘要")


if __name__ == "__main__":
    unittest.main()
