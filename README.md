# arXiv Papers: Speech, Audio, Music

每日自动抓取 arXiv 上与 **语音、音频、音乐** 相关的最新论文。

## 数据来源
- arXiv 分类: `cs.SD` (Sound), `eess.AS` (Audio & Speech), `cs.LG` (Machine Learning), `cs.AI`
- 关键词过滤: speech, audio, music, voice, sound, Mel, representation, self-supervised...
- 更新频率: 每日 UTC 02:00 (约北京时间 10:00)

## 最新数据
- 查看 [papers/latest/](papers/latest/) 获取最新一天的论文

## 按日期浏览
| 日期 | 论文数 | 查看 |
|------|--------|------|
| 运行后自动生成 | | |

## 文件结构
```
papers/
├── 2025-01-28/
│   ├── 2501.01108.json
│   ├── 2501.01109.json
│   └── README.md  (当日综述)
├── 2025-01-29/
└── latest -> 2025-01-28  (符号链接)
```

## 自动化
- 使用 GitHub Actions 每日自动运行
- 配置: [`.github/workflows/daily.yml`](.github/workflows/daily.yml)

## 本地运行
```bash
# 安装依赖
pip install -r requirements.txt

# 运行（测试模式）
python arxiv_monitor.py

# 首次运行前确保Git可写
git remote -v  # 应显示 origin git@github.com:786440445/arxiv-papers.git
```

## 自定义
修改 `config.yaml` 调整：
- 监控的 arXiv 分类
- 关键词过滤规则
- Git 提交信息模板

## 许可证
数据来源于 arXiv，遵循 [arXiv 使用政策](https://arxiv.org/help/license)。

---

**注意**：首次运行前请确保：
1. GitHub仓库已创建：https://github.com/786440445/arxiv-papers.git
2. 本地已配置SSH密钥并添加到GitHub
3. 运行 `git remote -v` 验证可写权限