#!/usr/bin/env python3
"""
Render daily and root README files from stored paper JSON files.
"""

import json
import os
import sys
from pathlib import Path


FALLBACK_SUMMARY_ZH = "中文摘要翻译失败，请查看原文 JSON。"


def iter_paper_files(date_dir):
    return sorted(date_dir.glob("*.json"))


def load_papers(date_dir):
    papers = []
    for paper_file in iter_paper_files(date_dir):
        paper = json.loads(paper_file.read_text(encoding="utf-8"))
        papers.append(paper)
    papers.sort(
        key=lambda paper: (
            paper.get("published", ""),
            paper.get("title", ""),
        ),
        reverse=True,
    )
    return papers


def format_authors(authors):
    if isinstance(authors, list):
        return ", ".join(authors)
    return authors or ""


def render_daily_readme(date_dir):
    papers = load_papers(date_dir)
    lines = [
        f"# arXiv Papers - {date_dir.name}",
        "",
        f"**来源**: arXiv",
        f"**今日新论文**: {len(papers)} 篇",
        "",
        "---",
        "",
    ]

    for index, paper in enumerate(papers, start=1):
        summary_zh = (paper.get("summary_zh") or "").strip() or FALLBACK_SUMMARY_ZH
        lines.extend(
            [
                f"## {index}. {paper.get('title', '')}",
                "",
                f"**Authors**: {format_authors(paper.get('authors'))}",
                f"**Categories**: {paper.get('category', '')}",
                f"**Published**: {paper.get('published', '')}",
                f"**Link**: {paper.get('link', '')}",
                f"**PDF**: {paper.get('pdf', '')}",
                "",
                "**摘要（中文）**:",
                f"> {summary_zh}",
                "",
                "---",
                "",
            ]
        )

    readme_path = date_dir / "README.md"
    readme_path.write_text("\n".join(lines), encoding="utf-8")
    return readme_path


def list_date_dirs(base_dir):
    return sorted(
        [
            path
            for path in base_dir.iterdir()
            if path.is_dir() and path.name[:1].isdigit()
        ],
        key=lambda path: path.name,
        reverse=True,
    )


def update_root_readme(base_dir, root_readme):
    date_dirs = list_date_dirs(base_dir)
    lines = [
        "# arXiv Papers: Speech, Audio, Music",
        "",
        "每日跟踪 arXiv 语音、音频、音乐相关论文。",
        "",
    ]

    if date_dirs:
        latest = date_dirs[0]
        count = len(iter_paper_files(latest))
        lines.extend(
            [
                "## Latest",
                "",
                f"- **{latest.name}**: [{count} papers](papers/latest/) (cs.SD, eess.AS, cs.LG, cs.AI)",
                "",
            ]
        )

    lines.extend(
        [
            "## All Dates",
            "",
            "| Date | Papers | View |",
            "|------|--------|------|",
        ]
    )

    for date_dir in date_dirs:
        count = len(iter_paper_files(date_dir))
        lines.append(f"| {date_dir.name} | {count} | [📖](papers/{date_dir.name}/) |")

    lines.append("")
    root_readme.write_text("\n".join(lines), encoding="utf-8")
    return root_readme


def update_latest_symlink(base_dir, date_str):
    latest_link = base_dir / "latest"
    target_name = date_str
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    os.symlink(target_name, latest_link)
    return latest_link


def render_all(date_str, base_dir=Path("papers"), root_readme=Path("README.md")):
    base_dir = Path(base_dir)
    date_dir = base_dir / date_str
    if not date_dir.exists():
        raise FileNotFoundError(f"{date_dir} not found")

    render_daily_readme(date_dir)
    update_root_readme(base_dir, Path(root_readme))
    update_latest_symlink(base_dir, date_str)


def main():
    if len(sys.argv) < 2:
        print("Usage: python render_daily.py <date>")
        print("Example: python render_daily.py 2026-03-26")
        print("Or: python render_daily.py today")
        sys.exit(1)

    date_arg = sys.argv[1]
    if date_arg == "today":
        from datetime import datetime

        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        date_str = date_arg

    render_all(date_str)


if __name__ == "__main__":
    main()
