#!/usr/bin/env python3
"""
arXiv Daily Monitor (Simplified - No Translation)
只抓取和保存，翻译由独立脚本处理
"""

import os
import sys
import json
import feedparser
import datetime
import subprocess
import logging
import yaml
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('arxiv_monitor.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

class ArxivMonitor:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

        self.seen_file = Path(self.config['arxiv']['seen_file'])
        self.output_dir = Path('papers')
        self.seen_ids = self.load_seen()

    def load_seen(self):
        if self.seen_file.exists():
            try:
                with open(self.seen_file, 'r', encoding='utf-8') as f:
                    return set(json.load(f))
            except Exception as e:
                logger.warning(f"Failed to load seen file: {e}")
                return set()
        return set()

    def save_seen(self):
        self.seen_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.seen_file, 'w', encoding='utf-8') as f:
            json.dump(list(self.seen_ids), f, indent=2, ensure_ascii=False)

    def fetch_rss(self, category):
        url = f"https://arxiv.org/rss/{category}"
        try:
            feed = feedparser.parse(url)
            papers = []
            for entry in feed.entries:
                paper_id = entry.id.split('/')[-1]
                papers.append({
                    'id': paper_id,
                    'title': entry.title,
                    'authors': entry.author,
                    'summary': entry.summary,
                    'published': entry.published,
                    'link': entry.link,
                    'pdf': f"https://arxiv.org/pdf/{paper_id}.pdf",
                    'category': category,
                    'fetched_at': datetime.datetime.now().isoformat(),
                })
            logger.info(f"Fetched {len(papers)} papers from {category}")
            return papers
        except Exception as e:
            logger.error(f"Error fetching {category}: {e}")
            return []

    def matches_keywords(self, paper):
        kw_cfg = self.config['arxiv']['keywords']
        text = (paper['title'] + ' ' + paper['summary']).lower()

        if not any(kw.lower() in text for kw in kw_cfg['include']):
            return False

        for kw in kw_cfg.get('exclude', []):
            if kw.lower() in text:
                return False

        return True

    def fetch_all_papers(self):
        all_papers = []
        categories = self.config['arxiv']['categories']

        for cat in categories:
            papers = self.fetch_rss(cat)
            all_papers.extend(papers)

        unique = {}
        for p in all_papers:
            if p['id'] not in unique:
                unique[p['id']] = p

        new_papers = [p for p in unique.values() if p['id'] not in self.seen_ids]
        filtered = [p for p in new_papers if self.matches_keywords(p)]

        logger.info(f"Total: {len(all_papers)}, New: {len(new_papers)}, Filtered: {len(filtered)}")
        return filtered

    def save_papers(self, papers, date_str):
        date_dir = self.output_dir / date_str
        date_dir.mkdir(parents=True, exist_ok=True)

        # 保存单篇JSON
        for p in papers:
            json_path = date_dir / f"{p['id']}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(p, f, indent=2, ensure_ascii=False)

        # 生成英文README（稍后翻译脚本会处理）
        readme_en = self.generate_readme_en(papers, date_str)
        with open(date_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_en)

        # 更新latest符号链接
        latest_link = self.output_dir / 'latest'
        if latest_link.exists() or latest_link.is_symlink():
            latest_link.unlink()
        latest_link.symlink_to(date_str, target_is_directory=True)

        # 更新总README
        self.update_main_readme()

        logger.info(f"Saved {len(papers)} papers to {date_dir}")

    def generate_readme_en(self, papers, date_str):
        """生成英文README（无翻译）"""
        md = f"""# arXiv Papers - {date_str}

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: {len(papers)} 篇

---

"""
        for i, p in enumerate(papers, 1):
            authors = p['authors'][:100] + '...' if len(p['authors']) > 100 else p['authors']
            md += f"""## {i}. {p['title']}

**Authors**: {authors}  
**Categories**: {p['category']}  
**Published**: {p['published']}  
**Link**: {p['link']}  
**PDF**: {p['pdf']}

**Abstract**:
> {p['summary'][:800]}{'...' if len(p['summary']) > 800 else ''}

---

"""
        return md

    def update_main_readme(self):
        main_readme = self.output_dir / "README.md"
        dates = sorted([d.name for d in self.output_dir.iterdir()
                       if d.is_dir() and d.name[0].isdigit()], reverse=True)

        content = "# arXiv Papers: Speech, Audio, Music\n\n"
        content += "每日跟踪 arXiv 语音、音频、音乐相关论文。\n\n"
        content += "## Latest\n\n"
        if dates:
            latest = dates[0]
            count = len(list((self.output_dir / latest).glob('*.json')))
            content += f"- **{latest}**: [{count} papers](papers/latest/) (cs.SD, eess.AS, cs.LG, cs.AI)\n\n"

        content += "## All Dates\n\n"
        content += "| Date | Papers | View |\n"
        content += "|------|--------|------|\n"

        for date in dates[:30]:
            count = len(list((self.output_dir / date).glob('*.json')))
            content += f"| {date} | {count} | [📖](papers/{date}/) |\n"

        with open(main_readme, 'w', encoding='utf-8') as f:
            f.write(content)

    def git_push(self, date_str, paper_count):
        try:
            result = subprocess.run(['git', 'status', '--porcelain'],
                                   capture_output=True, text=True, cwd='.')
            if not result.stdout.strip():
                logger.info("No changes to commit")
                return False

            subprocess.run(['git', 'add', 'papers/'], check=True, cwd='.')
            subprocess.run(['git', 'add', '.seen_papers.json'], check=True, cwd='.')
            subprocess.run(['git', 'add', 'README.md'], check=True, cwd='.')

            commit_msg = self.config['github']['commit_template'].format(
                date=date_str, count=paper_count
            )
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True, cwd='.')

            subprocess.run(['git', 'push', 'origin', self.config['github']['branch']],
                          check=True, cwd='.', env={'GIT_SSH_COMMAND': 'ssh -o StrictHostKeyChecking=no'})

            logger.info(f"Pushed {paper_count} papers to GitHub")
            return True

        except subprocess.CalledProcessError as e:
            logger.error(f"Git error: {e}")
            return False

    def send_feishu_notification(self, papers):
        if not papers:
            logger.info("No papers to notify")
            return

        cfg = self.config['feishu']
        if cfg['target_type'] == 'self':
            self.send_to_self(papers, cfg['format'])
        else:
            self.send_to_chat(papers, cfg['chat_id'], cfg['format'])

    def send_to_self(self, papers, format_type):
        """发送通知给当前用户"""
        if format_type == 'summary':
            msg = f"📚 **arXiv Daily Digest**\n"
            msg += f"发现 **{len(papers)}** 篇新论文\n\n"

            for i, p in enumerate(papers[:5], 1):
                title = p['title'][:60] + ("..." if len(p['title']) > 60 else "")
                msg += f"{i}. **{title}**\n"
                msg += f"   ID: {p['id']}\n"
                msg += f"   {p['link']}\n\n"

            if len(papers) > 5:
                msg += f"... 还有 {len(papers)-5} 篇\n"

            msg += f"\n详情: https://github.com/786440445/arxiv-papers/tree/main/papers/latest"

        else:
            msg = f"📚 **arXiv Full List ({len(papers)} papers)**\n\n"
            for i, p in enumerate(papers[:10], 1):
                title = p['title'][:80]
                msg += f"{i}. {title}\n   ID: {p['id']}\n   {p['link']}\n\n"
            if len(papers) > 10:
                msg += f"... 还有 {len(papers)-10} 篇，请查看GitHub仓库\n"

        try:
            from openclaw import message as send_message
            send_message(action="send", channel="feishu", message=msg)
            logger.info("Sent Feishu notification")
        except Exception as e:
            logger.error(f"Failed to send Feishu message: {e}")

    def send_to_chat(self, papers, chat_id, format_type):
        pass

    def run(self):
        logger.info("Starting arXiv monitor...")
        papers = self.fetch_all_papers()
        if not papers:
            logger.info("No new papers today!")
            return

        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        self.save_papers(papers, date_str)
        self.git_push(date_str, len(papers))
        self.send_feishu_notification(papers)

        for p in papers:
            self.seen_ids.add(p['id'])
        self.save_seen()

        logger.info(f"Done! Processed {len(papers)} papers.")

def main():
    try:
        monitor = ArxivMonitor()
        monitor.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()