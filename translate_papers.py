#!/usr/bin/env python3
"""
Translate daily arXiv paper abstracts into Chinese with OpenRouter.
"""

import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "stepfun/step-3.5-flash:free"
DEFAULT_TIMEOUT = 120


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def build_messages(title, summary):
    return [
        {
            "role": "system",
            "content": (
                "You are a precise academic translator. Translate the paper abstract "
                "into formal Simplified Chinese. Output only the translated abstract."
            ),
        },
        {
            "role": "user",
            "content": f"Title: {title}\n\nAbstract:\n{summary}",
        },
    ]


def extract_message_content(payload):
    choices = payload.get("choices") or []
    if not choices:
        raise ValueError("OpenRouter response missing choices")

    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        content = content.strip()
    if not content:
        raise ValueError("OpenRouter response missing message content")
    return content


def request_translation(title, summary, api_key, timeout=DEFAULT_TIMEOUT):
    payload = {
        "model": MODEL_NAME,
        "messages": build_messages(title, summary),
    }
    request = Request(
        OPENROUTER_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urlopen(request, timeout=timeout) as response:
        response_payload = json.loads(response.read().decode("utf-8"))
    return extract_message_content(response_payload)


def iter_paper_files(date_dir):
    return sorted(
        path
        for path in date_dir.glob("*.json")
        if path.name != "translations.json"
    )


def translate_paper_file(path, api_key, timeout=DEFAULT_TIMEOUT):
    paper = json.loads(path.read_text(encoding="utf-8"))
    summary = (paper.get("summary") or "").strip()
    if not summary:
        logger.info("Skipping %s because summary is empty", path.name)
        return False
    if paper.get("summary_zh"):
        logger.info("Skipping %s because summary_zh already exists", path.name)
        return False

    translation = request_translation(
        title=paper.get("title", ""),
        summary=summary,
        api_key=api_key,
        timeout=timeout,
    )
    paper["summary_zh"] = translation
    paper["translation_model"] = MODEL_NAME
    paper["translation_updated_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(
        json.dumps(paper, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info("Translated %s", path.name)
    return True


def translate_date_papers(date_str, base_dir=Path("papers"), api_key=None, timeout=DEFAULT_TIMEOUT):
    api_key = api_key or os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is required")

    date_dir = Path(base_dir) / date_str
    if not date_dir.exists():
        raise FileNotFoundError(f"{date_dir} not found")

    translated = 0
    skipped = 0
    failed = 0

    for paper_file in iter_paper_files(date_dir):
        try:
            changed = translate_paper_file(paper_file, api_key=api_key, timeout=timeout)
            if changed:
                translated += 1
            else:
                skipped += 1
        except Exception as exc:
            failed += 1
            logger.warning("Failed to translate %s: %s", paper_file.name, exc)

    logger.info(
        "Translation complete for %s: translated=%s skipped=%s failed=%s",
        date_str,
        translated,
        skipped,
        failed,
    )
    return {
        "translated": translated,
        "skipped": skipped,
        "failed": failed,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_papers.py <date>")
        print("Example: python translate_papers.py 2026-03-26")
        print("Or: python translate_papers.py today")
        sys.exit(1)

    date_arg = sys.argv[1]
    if date_arg == "today":
        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        date_str = date_arg

    translate_date_papers(date_str)


if __name__ == "__main__":
    main()
