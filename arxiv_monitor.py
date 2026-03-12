#!/usr/bin/env python3
"""
arXiv Daily Monitor with Chinese Translation
语音相关论文监控，自动翻译标题和摘要为中文
"""

import os
import sys
import json
import feedparser
import datetime
import subprocess
import logging
import yaml
import re
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

# 中英翻译映射（学术/技术常用词）
TRANSLATION_MAP = {
    # 基础术语
    'paper': '论文', 'technical report': '技术报告', 'preprint': '预印本',
    'author': '作者', 'university': '大学', 'lab': '实验室', 'institute': '研究所',
    'introduction': '引言', 'abstract': '摘要', 'section': '节', 'appendix': '附录',
    'acknowledgment': '致谢', 'conclusion': '结论', 'future work': '未来工作',
    'neural': '神经', 'network': '网络', 'deep': '深度', 'learning': '学习',
    'training': '训练', 'inference': '推理', 'dataset': '数据集', 'corpus': '语料库',
    'sampling': '采样', 'optimization': '优化', 'loss': '损失', 'gradient': '梯度',
    'feature': '特征', 'representation': '表示', 'embedding': '嵌入', 'vector': '向量',
    'classification': '分类', 'detection': '检测', 'recognition': '识别',
    'segmentation': '分割', 'generation': '生成', 'synthesis': '合成',
    'speech': '语音', 'audio': '音频', 'music': '音乐', 'sound': '声音',
    'emotion': '情感', 'voice': '声纹', 'speaker': '说话人', 'lip': '唇部',
    'video': '视频', 'image': '图像', 'visual': '视觉',
    'real-time': '实时', 'efficient': '高效', 'robust': '鲁棒', 'accurate': '准确',
    'model': '模型', 'architecture': '架构', 'framework': '框架', 'system': '系统',
    'algorithm': '算法', 'method': '方法', 'approach': '方案', 'technique': '技术',
    'performance': '性能', 'result': '结果', 'experiment': '实验', 'evaluation': '评估',
    'benchmark': '基准', 'dataset': '数据集', 'implementation': '实现',
    'code': '代码', 'open source': '开源', 'github': 'GitHub',
    'transformer': 'Transformer', 'attention': '注意力', 'convolution': '卷积',
    'recurrent': '循环', 'lstm': 'LSTM', 'gru': 'GRU', 'cnn': 'CNN', 'rnn': 'RNN',
    'llm': '大语言模型', 'gpt': 'GPT', 'claude': 'Claude', 'gemini': 'Gemini',
    'llama': 'LLaMA', 'mistral': 'Mistral', 'qwen': '通义千问',
    'arxiv': 'arXiv', 'submission': '提交', 'revision': '修订', 'accept': '接收',
    'reject': '拒绝', 'review': '审稿', 'meta-review': '总结审稿',
    'title': '标题', 'link': '链接', 'published': '发布日期', 'updated': '更新日期',
    'category': '分类', 'journal': '期刊', 'conference': '会议',
    'self-supervised': '自监督', 'unsupervised': '无监督', 'supervised': '有监督',
    'semi-supervised': '半监督', 'few-shot': '少样本', 'zero-shot': '零样本',
    'multi-modal': '多模态', 'cross-lingual': '跨语言', 'multi-task': '多任务',
    'contrastive': '对比', 'adversarial': '对抗', 'probabilistic': '概率',
    'bayesian': '贝叶斯', 'graphical model': '图模型', 'latent': '隐变量',
    'generative': '生成式', 'discriminative': '判别式', 'causal': '因果',
    'explainable': '可解释', 'interpretable': '可解释', 'trustworthy': '可信',
    'fairness': '公平性', 'bias': '偏见', 'ethics': '伦理',
    'privacy': '隐私', 'secure': '安全', 'robustness': '鲁棒性',
    'out-of-distribution': '分布外', 'generalization': '泛化',
    'transfer learning': '迁移学习', 'domain adaptation': '领域适应',
    'federated learning': '联邦学习', 'edge computing': '边缘计算',
    'cloud': '云端', 'deployment': '部署', 'serving': '服务',
    'streaming': '流式', 'online': '在线', 'offline': '离线',
    'distributed': '分布式', 'parallel': '并行', 'scalable': '可扩展',
    'low-latency': '低延迟', 'high-throughput': '高吞吐',
    'nlp': '自然语言处理', 'cv': '计算机视觉', 'asr': '自动语音识别',
    'tts': '文本转语音', 'vc': '语音转换', 'se': '说话人识别',
    'kws': '关键词检测', 'sid': '说话人识别', 'asr': '语音识别',
    'mt': '机器翻译', 'summarization': '摘要', 'qa': '问答',
    'recommendation': '推荐', 'search': '搜索', 'retrieval': '检索',
    'knowledge graph': '知识图谱', 'ontology': '本体',
    'reasoning': '推理', 'planning': '规划', 'decision': '决策',
    'control': '控制', 'robotics': '机器人', 'autonomous': '自主',
    'agent': '智能体', 'multi-agent': '多智能体', 'swarm': '群体',
    'evolution': '进化', 'optimization': '优化', 'search': '搜索',
    'genetic': '遗传', 'mutation': '变异', 'crossover': '交叉',
    'selection': '选择', 'population': '种群', 'fitness': '适应度',
    'reinforcement': '强化', 'policy': '策略', 'value': '价值',
    'reward': '奖励', 'environment': '环境', 'state': '状态',
    'action': '动作', 'observation': '观测', 'transition': '转移',
    'discount': '折扣', 'return': '回报', 'advantage': '优势',
    'actor-critic': '演员-评论员', 'dqn': 'DQN', 'ppo': 'PPO',
    'sac': 'SAC', 'td3': 'TD3', 'a2c': 'A2C', 'trpo': 'TRPO',
    'ils': 'ILS', 'mcts': 'MCTS', 'gradient': '梯度',
    'policy gradient': '策略梯度', 'value-based': '基于价值',
    'model-based': '基于模型', 'model-free': '无模型',
    'on-policy': '同策略', 'off-policy': '异策略',
    'actor': '演员', 'critic': '评论员', 'target': '目标',
    'experience replay': '经验回放', 'buffer': '缓冲区',
    'prioritized': '优先', 'episode': '回合', 'trajectory': '轨迹',
    'horizon': '视野', 'discount factor': '折扣因子',
    'exploration': '探索', 'exploitation': '利用', 'balance': '平衡',
    'entropy': '熵', 'regularization': '正则化', 'normalization': '归一化',
    'batch': '批次', 'epoch': '轮次', 'iteration': '迭代',
    'learning rate': '学习率', 'scheduler': '调度器', 'optimizer': '优化器',
    'sgd': 'SGD', 'adam': 'Adam', 'rmsprop': 'RMSprop', 'adagrad': 'Adagrad',
    'momentum': '动量', 'weight decay': '权重衰减', 'clip': '截断',
    'gradient descent': '梯度下降', 'ascent': '上升',
    'backpropagation': '反向传播', 'forward': '前向', 'backward': '反向',
    'autograd': '自动微分', 'dynamic': '动态', 'static': '静态',
    'computation graph': '计算图', 'tape': '磁带', 'vectorized': '向量化',
    'jax': 'JAX', 'tensorflow': 'TensorFlow', 'pytorch': 'PyTorch',
    'keras': 'Keras', 'theano': 'Theano', 'caffe': 'Caffe',
    'mxnet': 'MXNet', 'paddlepaddle': 'PaddlePaddle', 'mindspore': 'MindSpore',
    'cpu': 'CPU', 'gpu': 'GPU', 'tpu': 'TPU', ' accelerator': '加速器',
    'memory': '内存', 'storage': '存储', 'disk': '磁盘',
    'bandwidth': '带宽', 'latency': '延迟', 'throughput': '吞吐量',
    'parallelism': '并行', 'distributed': '分布式', 'cluster': '集群',
    'node': '节点', 'server': '服务器', 'client': '客户端',
    'api': 'API', 'rest': 'REST', 'grpc': 'gRPC', 'graphql': 'GraphQL',
    'json': 'JSON', 'xml': 'XML', 'yaml': 'YAML', 'toml': 'TOML',
    'encode': '编码', 'decode': '解码', 'serialize': '序列化',
    'deserialize': '反序列化', 'compress': '压缩', 'decompress': '解压',
    'encrypt': '加密', 'decrypt': '解密', 'hash': '哈希',
    'signature': '签名', 'certificate': '证书', 'ssl': 'SSL', 'tls': 'TLS',
    'authentication': '认证', 'authorization': '授权', 'access control': '访问控制',
    'permission': '权限', 'role': '角色', 'policy': '策略',
    'firewall': '防火墙', 'vpn': 'VPN', 'proxy': '代理',
}

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

    def translate_text(self, text):
        """将英文文本翻译为中文（基于关键词映射）"""
        if not text or len(text.strip()) == 0:
            return text
        # 如果已经包含中文，直接返回
        if any('\u4e00' <= c <= '\u9fff' for c in text):
            return text
        try:
            result = text
            # 执行全局替换（不区分大小写）
            for en, zh in TRANSLATION_MAP.items():
                pattern = re.compile(r'\b' + re.escape(en) + r'\b', re.IGNORECASE)
                result = pattern.sub(zh, result)
            return result
        except Exception as e:
            logger.warning(f"Translation error: {e}, returning original")
            return text

    def fetch_rss(self, category):
        """获取单个类别的RSS"""
        url = f"https://arxiv.org/rss/{category}"
        try:
            feed = feedparser.parse(url)
            return feed
        except Exception as e:
            logger.error(f"Failed to fetch RSS for {category}: {e}")
            return None

    def fetch_all_papers(self):
        """从所有类别抓取论文"""
        categories = self.config['arxiv']['categories']
        papers = []

        for category in categories:
            feed = self.fetch_rss(category)
            if not feed or not feed.entries:
                continue

            for entry in feed.entries:
                try:
                    paper_id = entry.id.split('/')[-1]
                    if paper_id in self.seen_ids:
                        continue

                    # 提取摘要
                    summary = getattr(entry, 'summary', '')

                    paper = {
                        'id': paper_id,
                        'title': entry.title,
                        'authors': [a.name for a in getattr(entry, 'authors', [])],
                        'category': category,
                        'link': f"https://arxiv.org/abs/{paper_id}",
                        'published': entry.published,
                        'summary': summary,
                    }
                    papers.append(paper)
                except Exception as e:
                    logger.warning(f"Failed to parse entry: {e}")
                    continue

        # 按发布日期排序（新的在前）
        papers.sort(key=lambda x: x['published'], reverse=True)
        return papers

    def save_papers(self, papers, date_str):
        """保存论文到本地文件系统"""
        date_dir = self.output_dir / date_str
        date_dir.mkdir(parents=True, exist_ok=True)

        for p in papers:
            # 翻译标题和摘要
            p['title_zh'] = self.translate_text(p['title'])
            p['summary_zh'] = self.translate_text(p['summary'])

            json_path = date_dir / f"{p['id']}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(p, f, indent=2, ensure_ascii=False)

        # 生成 README.md
        readme_path = date_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"# arXiv Papers - {date_str}\n\n")
            f.write(f"**论文数量**: {len(papers)}\n\n")
            for i, p in enumerate(papers, 1):
                f.write(f"## {i}. {p['title_zh']}\n\n")
                f.write(f"**原标题**: {p['title']}\n\n")
                f.write(f"**作者**: {', '.join(p['authors'][:5])}\n")
                if len(p['authors']) > 5:
                    f.write(f"（还有 {len(p['authors'])-5} 位作者）\n")
                f.write(f"**分类**: {p['category']}\n")
                f.write(f"**发布时间**: {p['published']}\n")
                f.write(f"**链接**: {p['link']}\n\n")
                if p['summary_zh']:
                    f.write(f"**中文摘要**:\n> {p['summary_zh'][:800]}{'...' if len(p['summary_zh']) > 800 else ''}\n\n")
                if p['summary']:
                    f.write(f"**Original Abstract**:\n> {p['summary'][:800]}{'...' if len(p['summary']) > 800 else ''}\n\n")
                f.write("---\n\n")

        logger.info(f"Saved {len(papers)} papers to {date_dir}")

    def git_push(self, date_str, count):
        """Git 提交并推送（如果配置了）"""
        try:
            # 检查是否初始化了 git
            if not (Path('.git').exists()):
                logger.info("Not a git repository, skipping push")
                return

            # 提交
            subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            msg = f"Update {date_str}: {count} new papers"
            subprocess.run(['git', 'commit', '-m', msg], check=True, capture_output=True)

            # 推送到远程
            remote = self.config['arxiv'].get('git_remote', 'origin')
            branch = self.config['arxiv'].get('git_branch', 'main')
            subprocess.run(['git', 'push', remote, branch], check=True, capture_output=True)
            logger.info(f"Git push successful: {count} papers")
        except subprocess.CalledProcessError as e:
            logger.error(f"Git error: {e.stderr.decode() if e.stderr else str(e)}")
        except Exception as e:
            logger.error(f"Git push failed: {e}")

    def send_feishu_notification(self, papers):
        """发送飞书通知"""
        if not papers:
            logger.info("No papers to notify")
            return

        if 'feishu' not in self.config:
            logger.info("Feishu config not found, skipping notification")
            return

        cfg = self.config['feishu']
        if cfg['target_type'] == 'self':
            self.send_to_self(papers, cfg['format'])
        else:
            self.send_to_chat(papers, cfg['chat_id'], cfg['format'])

    def send_to_self(self, papers, format_type):
        """发送通知给当前用户（通过print，cron会捕获）"""
        if format_type == 'summary':
            msg = f"# 📚 arXiv 语音相关论文每日推送\n\n"
            msg += f"**日期**: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
            msg += f"**发现新论文**: {len(papers)} 篇\n\n"

            for i, p in enumerate(papers[:5], 1):
                title_zh = p.get('title_zh', self.translate_text(p['title']))
                title_disp = title_zh[:60] + ("..." if len(title_zh) > 60 else "")
                msg += f"{i}. **{title_disp}**\n"
                msg += f"   ID: {p['id']}\n"
                summary_zh = p.get('summary_zh', self.translate_text(p.get('summary', '')))
                if summary_zh:
                    msg += f"   💡 摘要: {summary_zh[:120]}...\n"
                msg += f"   🔗 {p['link']}\n\n"

            if len(papers) > 5:
                msg += f"... 还有 {len(papers)-5} 篇，请查看 GitHub 仓库：https://github.com/786440445/arxiv-papers/tree/main/papers/latest"
            else:
                msg += "今日所有论文已列出 above."
        else:
            msg = f"# 📚 arXiv Full List ({len(papers)} papers)\n\n"
            for i, p in enumerate(papers[:10], 1):
                title_zh = p.get('title_zh', self.translate_text(p['title']))
                msg += f"{i}. {title_zh[:80]}\n   ID: {p['id']}\n   {p['link']}\n\n"
            if len(papers) > 10:
                msg += f"... 还有 {len(papers)-10} 篇，请查看GitHub仓库\n"

        # 打印，cron 会捕获 stdout
        print(msg)
        logger.info("Sent notification to stdout (cron)")

    def send_to_chat(self, papers, chat_id, format_type):
        pass

    def update_root_readme(self):
        """更新项目根目录的 README.md（可选）"""
        root_readme = Path('README.md')
        if not root_readme.exists():
            return

        dates = sorted([d.name for d in self.output_dir.iterdir()
                       if d.is_dir() and d.name[0].isdigit()], reverse=True)

        content = "# arXiv Papers: Speech, Audio, Music\n\n"
        content += "每日跟踪 arXiv 语音、音频、音乐相关论文。\n\n"

        if dates:
            latest = dates[0]
            count = len(list((self.output_dir / latest).glob('*.json')))
            content += f"## Latest\n\n- **{latest}**: [{count} papers](papers/latest/) (cs.SD, eess.AS, cs.LG, cs.AI)\n\n"

        content += "## All Dates\n\n"
        content += "| Date | Papers | View |\n"
        content += "|------|--------|------|\n"

        for date in dates[:30]:
            count = len(list((self.output_dir / date).glob('*.json')))
            content += f"| {date} | {count} | [📖](papers/{date}/) |\n"

        with open(root_readme, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"Updated root README.md")

    def run(self):
        """主运行流程"""
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

        # 为 cron 输出摘要（已经包含在 send_feishu_notification 的 print 中）
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
