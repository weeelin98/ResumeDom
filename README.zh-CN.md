# ResumeReviewer

<p align="center">
  <a href="README.md">English</a> ·
  <b>简体中文</b>
</p>

ResumeReviewer 是面向美国科技岗位的 Codex 简历 skill，主要服务计算机专业实习生和应届毕业生。它将可复用的真实经历证据与针对单个岗位的投递内容严格分开。

## 两种简历模式

### 1. Core Resume（真实核心简历）

建立完整的事实资料库，包括经过确认的工作经历、CAR 故事、项目、技术范围和成果。Core Resume 不针对某一条职位描述，生成投递版本时不得反向修改或污染它。

### 2. Application Resume（岗位投递简历）

分析单个职位描述，将岗位要求映射到 Core Resume 中已经验证的证据，选择最有说服力的内容，并生成针对该岗位的倒序简历。真实能力缺口必须明确保留，不能用虚构内容填补。

## 项目专属硬规则

- `Skills` 必须位于简历最后。
- 英文简历正文必须删除所有独立冠词 `a`、`an` 和 `the`。
- 最终简历不得使用 `led`、`managed` 或 `architected`。
- 经历和项目 bullet 使用过去时。
- 不得虚构指标、技术、日期、ownership、部署状态或业务结果。
- 真实指标不设置人为百分比上限；必要时补充基线、周期或范围以保证可信度。

## 从 GitHub 安装

### 在 Codex 中安装

对 Codex 发送：

```text
Use $skill-installer to install https://github.com/weeelin98/ResumeReviewer/tree/main/resume-reviewer
```

安装完成后，skill 将从下一轮对话开始可用。

### 使用内置安装脚本

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo weeelin98/ResumeReviewer \
  --path resume-reviewer
```

安装位置为 `${CODEX_HOME:-$HOME/.codex}/skills/resume-reviewer`。如果目标目录已经存在，需要先移动或删除旧版本，再重新安装。

### 链接本地开发仓库

如果希望执行 `git pull` 后立即使用最新版本，可以创建符号链接：

```bash
git clone https://github.com/weeelin98/ResumeReviewer.git
ln -s "$(pwd)/ResumeReviewer/resume-reviewer" "${CODEX_HOME:-$HOME/.codex}/skills/resume-reviewer"
```

仅在目标路径不存在时创建链接。安装或更新后，请开启新一轮 Codex 对话。

## 使用示例

建立 Core Resume：

```text
Use $resume-reviewer to turn my resume and raw project notes into a verified Core Resume for backend and AI/ML roles.
```

生成岗位投递简历：

```text
Use $resume-reviewer to tailor my Core Resume to this job description. Show requirement-to-proof map before final resume.
```

仅进行诊断：

```text
Use $resume-reviewer to diagnose ATS, credibility, and relevance problems without rewriting yet.
```

## 验证 Markdown 简历

```bash
python3 resume-reviewer/scripts/validate_resume.py path/to/resume.md
```

验证器会检查 Skills 位置、冠词、禁用动词、第一人称、空洞表达、未确认占位符、bullet 长度和重复开头动词。验证器只能辅助语言和结构检查，不能证明事实真实性。

## 仓库结构

```text
resume-reviewer/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── ats-and-layout.md
│   ├── evidence-and-car.md
│   ├── output-schema.md
│   └── role-competencies.md
└── scripts/validate_resume.py
```

`resumeReviewer.json` 作为兼容入口保留，供无法直接加载 Codex skill 的工具使用。

## 参考文献

- Laura DeCarlo，《*Resumes For Dummies*》，第 9 版，John Wiley & Sons，2026。主要参考 ATS、倒序格式、Core/OnTarget Resume、CAR 证据、AI 防幻觉、简历语言、新毕业生策略和最终审校相关章节。
- [OpenAI Developers：Codex use cases - Save workflows as skills](https://developers.openai.com/codex/use-cases)，用于 Codex skill 目录结构与使用方式参考。

本仓库不重新分发参考书 PDF。任何简历方法都不能保证 ATS 排名、面试或录用结果。
