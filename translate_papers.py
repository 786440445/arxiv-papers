#!/usr/bin/env python3
"""
批量翻译论文摘要（使用step-3.5-flash）
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# 添加OpenClaw路径
sys.path.insert(0, '/usr/local/lib/node_modules/openclaw')

def translate_text(text, title=""):
    """使用step-3.5-flash翻译"""
    try:
        from openclaw import sessions_spawn

        if title:
            prompt = f"""请将以下英文学术论文标题和摘要翻译成中文。

要求：
1. 标题翻译简洁准确（提供中文标题）
2. 摘要翻译完整、正式、学术化
3. 专有名词保留原文或通用译名
4. 直接输出，不要任何额外解释

输出格式：
中文标题：（翻译）
中文摘要：（翻译）

标题：{title[:200]}
摘要：{text[:800]}"""
        else:
            prompt = f"""请将以下英文学术论文摘要翻译成中文。

要求：
1. 翻译准确、正式、学术化
2. 保持专业术语一致性
3. 不添加任何解释

摘要：{text[:800]}"""

        result = sessions_spawn(
            task=prompt,
            model="custom/stepfun/step-3.5-flash:free",
            mode="run",
            timeoutSeconds=120
        )

        if result.get('status') == 'completed':
            return result.get('output', '').strip()
        else:
            return f"[翻译失败: {result.get('error', 'unknown')}]"

    except Exception as e:
        return f"[翻译错误: {str(e)}]"

def translate_date_papers(date_str):
    """翻译指定日期的所有论文"""
    date_dir = Path('papers') / date_str

    if not date_dir.exists():
        print(f"Error: {date_dir} not found")
        return

    json_files = sorted([f for f in date_dir.glob('*.json') if f.name != 'papers_list.json'])

    print(f"Found {len(json_files)} papers in {date_str}")

    # 加载现有翻译缓存
    cache_file = date_dir / 'translations.json'
    translations = {}
    if cache_file.exists():
        try:
            translations = json.load(open(cache_file, 'r', encoding='utf-8'))
            print(f"Loaded {len(translations)} cached translations")
        except:
            pass

    # 翻译每篇论文
    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                paper = json.load(f)

            paper_id = paper['id']
            title = paper['title']
            summary = paper['summary']

            # 检查是否已翻译
            if paper_id in translations:
                print(f"[{i}/{len(json_files)}] Skipping {paper_id} (cached)")
                continue

            print(f"[{i}/{len(json_files)}] Translating: {title[:60]}...")

            translation = translate_text(summary, title)
            translations[paper_id] = translation

            # 每篇都保存缓存
            json.dump(translations, open(cache_file, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

        except Exception as e:
            print(f"Error translating {json_file}: {e}")

    print(f"\n✓ Translations saved to {cache_file}")

    # 生成中文版README
    generate_chinese_readme(date_dir, translations)
    print(f"✓ Chinese README generated")

def generate_chinese_readme(date_dir, translations):
    """生成包含中文翻译的README"""
    json_files = sorted([f for f in date_dir.glob('*.json') if f.name != 'papers_list.json'])

    if not json_files:
        return

    # 读取第一份JSON获取日期（从文件名或内容）
    with open(json_files[0], 'r', encoding='utf-8') as f:
        sample = json.load(f)
        date_str = sample.get('published', date_dir.name)

    md = f"""# arXiv Papers - {date_dir.name}

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**今日新论文**: {len(json_files)} 篇

---

"""

    for i, json_file in enumerate(json_files[:20], 1):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                p = json.load(f)

            title = p.get('title', '')
            authors = p.get('authors', '')
            if isinstance(authors, list):
                authors = ', '.join(authors)
            authors = authors[:100] + '...' if len(authors) > 100 else authors
            summary = p.get('summary', '')
            categories = ', '.join(p.get('categories', []))
            link = p.get('link', 'N/A')
            pdf = p.get('pdf', 'N/A')

            translation = translations.get(p['id'], "[待翻译]")

            md += f"""## {i}. {title}

**Authors**: {authors}
**Categories**: {categories}
**Link**: {link}
**PDF**: {pdf}

**Abstract (EN)**:
> {summary[:800]}{'...' if len(summary) > 800 else ''}

**摘要（中文）**:
> {translation}

---

"""
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
            continue

    if len(json_files) > 20:
        md += f"\n... 还有 {len(json_files) - 20} 篇论文（完整列表见JSON文件）\n"

    readme_path = date_dir / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(md)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_papers.py <date>")
        print("Example: python translate_papers.py 2025-02-27")
        print("Or: python translate_papers.py today")
        sys.exit(1)

    date_arg = sys.argv[1]
    if date_arg == 'today':
        date_str = datetime.now().strftime('%Y-%m-%d')
    else:
        date_str = date_arg

    translate_date_papers(date_str)

if __name__ == '__main__':
    main()