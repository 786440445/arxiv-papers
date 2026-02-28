#!/usr/bin/env python3
"""
arXiv Daily Monitor for Speech, Audio, Music papers
自动抓取、保存到GitHub、发送通知
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
        """加载已处理的论文ID"""
        if self.seen_file.exists():
            try:
                with open(self.seen_file, 'r', encoding='utf-8') as f:
                    return set(json.load(f))
            except Exception as e:
                logger.warning(f"Failed to load seen file: {e}")
                return set()
        return set()

    def save_seen(self):
        """保存已处理ID"""
        self.seen_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.seen_file, 'w', encoding='utf-8') as f:
            json.dump(list(self.seen_ids), f, indent=2, ensure_ascii=False)

    def fetch_rss(self, category):
        """从arXiv RSS获取论文"""
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
        """检查论文是否匹配关键词"""
        kw_cfg = self.config['arxiv']['keywords']
        text = (paper['title'] + ' ' + paper['summary']).lower()

        # Include keywords
        if not any(kw.lower() in text for kw in kw_cfg['include']):
            return False

        # Exclude keywords
        for kw in kw_cfg.get('exclude', []):
            if kw.lower() in text:
                return False

        return True

    def fetch_all_papers(self):
        """抓取所有分类的论文"""
        all_papers = []
        categories = self.config['arxiv']['categories']

        for cat in categories:
            papers = self.fetch_rss(cat)
            all_papers.extend(papers)

        # 去重（同一篇可能在多个分类）
        unique = {}
        for p in all_papers:
            if p['id'] not in unique:
                unique[p['id']] = p

        # 过滤新论文
        new_papers = [p for p in unique.values() if p['id'] not in self.seen_ids]

        # 关键词过滤
        filtered = [p for p in new_papers if self.matches_keywords(p)]

        logger.info(f"Total: {len(all_papers)}, New: {len(new_papers)}, Filtered: {len(filtered)}")
        return filtered

    def save_papers(self, papers, date_str):
        """保存论文到本地"""
        date_dir = self.output_dir / date_str
        date_dir.mkdir(parents=True, exist_ok=True)

        # 保存单篇JSON
        for p in papers:
            json_path = date_dir / f"{p['id']}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(p, f, indent=2, ensure_ascii=False)

        # 生成README.md
        readme = self.generate_readme(papers, date_str)
        with open(date_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme)

        # 更新latest符号链接
        latest_link = self.output_dir / 'latest'
        if latest_link.exists() or latest_link.is_symlink():
            latest_link.unlink()
        latest_link.symlink_to(date_str, target_is_directory=True)

        # 更新总README
        self.update_main_readme()

        logger.info(f"Saved {len(papers)} papers to {date_dir}")

    def generate_readme(self, papers, date_str):
        """生成当日Markdown"""
        md = f"""# arXiv Papers - {date_str}

**Source**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)
**Keywords**: speech, audio, music, voice, sound, Mel, representation, self-supervised
**Total**: {len(papers)} new papers

---

"""

        for i, p in enumerate(papers, 1):
            title = p['title']
            authors = p['authors'][:100] + '...' if len(p['authors']) > 100 else p['authors']

            md += f"""## {i}. {title}

**ID**: {p['id']}
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
        """更新根目录README（列出所有日期）"""
        main_readme = self.output_dir / "README.md"

        # 收集所有日期文件夹
        dates = sorted([d.name for d in self.output_dir.iterdir()
                       if d.is_dir() and d.name[0].isdigit()], reverse=True)

        content = "# arXiv Papers: Speech, Audio, Music\n\n"
        content += "Daily monitoring of arXiv papers.\n\n"
        content += "## Latest\n\n"
        if dates:
            latest = dates[0]
            count = len(list((self.output_dir / latest).glob('*.json')))
            content += f"- **{latest}**: [{count} papers](papers/latest/) (cs.SD, eess.AS, cs.LG, cs.AI)\n\n"

        content += "## All Dates\n\n"
        content += "| Date | Papers | View |\n"
        content += "|------|--------|------|\n"

        for date in dates[:30]:  # 只显示最近30天
            count = len(list((self.output_dir / date).glob('*.json')))
            content += f"| {date} | {count} | [📖](papers/{date}/) |\n"

        with open(main_readme, 'w', encoding='utf-8') as f:
            f.write(content)

    def git_push(self, date_str, paper_count):
        """提交并推送到GitHub"""
        try:
            # 检查是否有变化
            result = subprocess.run(['git', 'status', '--porcelain'],
                                   capture_output=True, text=True, cwd='.')
            if not result.stdout.strip():
                logger.info("No changes to commit")
                return False

            # 添加文件
            subprocess.run(['git', 'add', 'papers/'], check=True, cwd=str(self.output_dir.parent))
            subprocess.run(['git', 'add', '.seen_papers.json'], check=True, cwd=str(self.output_dir.parent))
            subprocess.run(['git', 'add', 'README.md'], check=True, cwd=str(self.output_dir.parent))

            # 提交
            commit_msg = self.config['github']['commit_template'].format(
                date=date_str, count=paper_count
            )
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True, cwd='.')

            # 推送
            subprocess.run(['git', 'push', 'origin', self.config['github']['branch']],
                          check=True, cwd='.', env={'GIT_SSH_COMMAND': 'ssh -o StrictHostKeyChecking=no'})

            logger.info(f"Pushed {paper_count} papers to GitHub")
            return True

        except subprocess.CalledProcessError as e:
            logger.error(f"Git error: {e}")
            return False

    def send_feishu_notification(self, papers):
        """发送Feishu通知到当前聊天窗口"""
        if not papers:
            logger.info("No papers to notify")
            return

        cfg = self.config['feishu']

        if cfg['target_type'] == 'self':
            self.send_to_self(papers, cfg['format'], cfg.get('include_abstract', False))
        else:
            self.send_to_chat(papers, cfg['chat_id'], cfg['format'])

    def send_to_self(self, papers, format_type, include_abstract):
        """发送通知给当前用户（通过OpenClaw）"""
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

        else:  # full
            msg = f"📚 **arXiv Full List ({len(papers)} papers)**\n\n"
            for i, p in enumerate(papers[:10], 1):  # Feishu消息长度限制
                title = p['title'][:80]
                msg += f"{i}. {title}\n   ID: {p['id']}\n   {p['link']}\n\n"

            if len(papers) > 10:
                msg += f"... 还有 {len(papers)-10} 篇，请查看GitHub仓库\n"

        try:
            # 通过OpenClaw的message工具发送到当前Feishu会话
            from openclaw import message as send_message
            send_message(
                action="send",
                channel="feishu",
                message=msg
            )
            logger.info("Sent Feishu notification")
        except Exception as e:
            logger.error(f"Failed to send Feishu message: {e}")

    def send_to_chat(self, papers, chat_id, format_type):
        """发送到指定群聊（备用方案）"""
        # 实现类似，使用target参数
        pass

    def run(self):
        """主流程"""
        logger.info("Starting arXiv monitor...")

        # 1. 抓取
        papers = self.fetch_all_papers()
        if not papers:
            logger.info("No new papers today!")
            return

        # 2. 保存
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        self.save_papers(papers, date_str)

        # 3. Git提交
        self.git_push(date_str, len(papers))

        # 4. 通知
        self.send_feishu_notification(papers)

        # 5. 更新seen列表
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