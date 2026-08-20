# ResumeReviewer

<p align="center">
  <a href="README.md">English</a> ·
  <b>简体中文</b>
</p>

ResumeReviewer 是面向美国科技岗位的 Codex 简历 skill，主要服务计算机专业实习生和应届毕业生。它将经过验证的职业事实记录与针对单个岗位的投递内容严格分开，并提供可编辑的 LaTeX 投递简历模板。

## 功能

### 1. 简历评估与诊断

检查 ATS 可读性、证据质量、岗位相关性、表达、可信度、隐私和版式。评估基于证据，不声称能够预测客观 ATS 分数。

### 2. 简历修改

重写 bullet、删除空话、提高技术表达清晰度、统一时态并调整 section 结构，同时保持原始事实不变。

### 3. Core Resume Record 生成

将现有简历、原始笔记、代码仓库和候选人回答整理成内部事实记录，并区分 `VERIFIED`、`NEEDS CONFIRMATION` 和 `DO NOT USE`。

### 4. Application Resume 生成

从经过验证的事实中选择最强证据，为一次具体投递生成简洁的倒序简历。

### 5. 根据职位描述定制

提取 must-have、nice-to-have、岗位职责、工具和高频术语，并将要求与候选人证据映射为 `DIRECT`、`ADJACENT` 或 `GAP`。

### 6. 岗位能力映射

支持 Frontend、Backend、Full-Stack、AI/ML、Data、Cloud/DevOps/SRE、Mobile、Product 和 Project/Program 等方向。

### 7. 事实与可信度保护

禁止虚构职位、日期、技术、指标、用户、ownership、部署状态和业务结果。未确认内容不得进入正式投递版本。

### 8. 自动简历验证

检查 Skills 位置、英文冠词、禁用动词、第一人称、空洞表达、未确认占位符、bullet 长度和重复开头动词。

### 9. 可编辑 LaTeX 生成

使用可复用的 Times New Roman 投递简历模板，生成可编辑 `.tex`；环境支持时同时提供 PDF 预览。

## 两种简历模式

### Core Resume Record

Core Resume Record 是标记为 `Not for Submission` 的内部事实资料库。它保存完整的真实经历、来源、技术范围和未确认问题，不针对某个岗位或页数优化，生成投递版本时不得反向修改。

### Application Resume

Application Resume 只从已验证 Core 证据中选择内容，针对一个具体岗位生成。真实能力缺口必须明确保留，不能用虚构内容填补。

默认格式：

- 不使用 Summary；
- 不列 Coursework；
- 学校/公司左对齐，城市右对齐；
- 学位/官方职位位于第二行，日期右对齐；
- 每段 Experience 固定 3 条 bullet；
- 项目根据真实证据保留 2-4 条 bullet；
- Skills 必须位于最后。

## 项目专属硬规则

- `Skills` 必须位于简历最后。
- 英文简历正文必须删除所有独立冠词 `a`、`an` 和 `the`。
- 最终简历不得使用 `led`、`managed` 或 `architected`。
- 经历和项目 bullet 使用过去时。
- 不得虚构指标、技术、日期、ownership、部署状态或业务结果。
- 真实指标不设置人为百分比上限；必要时补充基线、周期或范围以保证可信度。

## LaTeX 模板

模板：[`resume-reviewer/assets/latex/application-resume.tex`](resume-reviewer/assets/latex/application-resume.tex)

默认排版：

- 系统安装 Times New Roman 时使用该字体，否则回退为 TeX Gyre Termes；
- 姓名 18 pt；
- section 标题 11 pt；
- 正文 10.5 pt；
- 联系方式保持一行；
- ATS 友好的单栏结构；
- 可复用的 Education、Experience、Project 和 bullet 宏。

使用 XeLaTeX 或 LuaLaTeX 编译：

```bash
cp resume-reviewer/assets/latex/application-resume.tex application-resume.tex
xelatex application-resume.tex
```

也可以使用 Tectonic：

```bash
tectonic -X compile application-resume.tex
```

填写个人信息前必须先复制模板，仓库中的模板应始终保持通用、无个人信息。

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

希望执行 `git pull` 后立即使用最新版本时，可以创建符号链接：

```bash
git clone https://github.com/weeelin98/ResumeReviewer.git
ln -s "$(pwd)/ResumeReviewer/resume-reviewer" "${CODEX_HOME:-$HOME/.codex}/skills/resume-reviewer"
```

仅在目标路径不存在时创建链接。安装或更新后，请开启新一轮 Codex 对话。

## 使用示例

只进行评估、不修改：

```text
Use $resume-reviewer to diagnose ATS, credibility, evidence, and relevance problems without rewriting yet.
```

建立 Core Resume Record：

```text
Use $resume-reviewer to turn my resume and raw project notes into a verified Core Resume Record for backend and AI/ML roles.
```

生成岗位投递简历：

```text
Use $resume-reviewer to tailor my Core Resume Record to this job description. Show requirement-to-proof map before final resume.
```

生成 LaTeX：

```text
Use $resume-reviewer to create an Application Resume from verified evidence and return editable LaTeX plus compiled PDF preview.
```

## 验证 Markdown 简历

```bash
python3 resume-reviewer/scripts/validate_resume.py path/to/resume.md
```

验证器用于辅助人工审核，不能证明事实真实性。

## 仓库结构

```text
resume-reviewer/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   └── latex/application-resume.tex
├── references/
│   ├── ats-and-layout.md
│   ├── evidence-and-car.md
│   ├── output-schema.md
│   ├── resume-templates.md
│   └── role-competencies.md
└── scripts/validate_resume.py
```

`resumeReviewer.json` 作为兼容入口保留，供无法直接加载 Codex skill 的工具使用。

## 参考文献

- Laura DeCarlo，《*Resumes For Dummies*》，第 9 版，John Wiley & Sons，2026。主要参考 ATS、倒序格式、Core/OnTarget Resume、CAR 证据、AI 防幻觉、简历语言、新毕业生策略和最终审校相关章节。
- [OpenAI Developers：Codex use cases - Save workflows as skills](https://developers.openai.com/codex/use-cases)，用于 Codex skill 目录结构与使用方式参考。

本仓库不重新分发参考书 PDF。任何简历方法都不能保证 ATS 排名、面试或录用结果。
