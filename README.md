# ResumeReviewer

<p align="center">
  <b>English</b> ·
  <a href="README.zh-CN.md">简体中文</a>
</p>

ResumeReviewer is a Codex skill for truthful, ATS-readable US technology resumes for computer-science interns and new graduates. It separates verified career records from job-specific application content and includes an editable LaTeX application-resume template.

## Capabilities

### 1. Resume assessment and diagnosis

Review ATS readability, evidence quality, relevance, wording, credibility, privacy, and layout. Assessment is evidence-based and does not claim to predict an objective ATS score.

### 2. Resume rewriting

Rewrite bullets, remove filler, improve technical clarity, standardize tense, and restructure sections without changing source truth.

### 3. Core Resume Record generation

Turn resumes, raw notes, repositories, and candidate answers into an internal factual record with `VERIFIED`, `NEEDS CONFIRMATION`, and `DO NOT USE` status.

### 4. Application Resume generation

Select strongest verified evidence and produce a concise reverse-chronological resume for one application.

### 5. Job-description tailoring

Parse must-haves, nice-to-haves, responsibilities, tools, and recurring terms. Map each requirement to candidate proof as `DIRECT`, `ADJACENT`, or `GAP`.

### 6. Role-competency mapping

Extract evidence for frontend, backend, full-stack, AI/ML, data, cloud/DevOps/SRE, mobile, product, and project/program roles.

### 7. Evidence and credibility safeguards

Prevent invented titles, dates, tools, metrics, users, ownership, deployment status, and business outcomes. Keep unresolved claims out of application-ready output.

### 8. Automated resume validation

Check Skills placement, English articles, forbidden verbs, first-person language, filler, unresolved placeholders, bullet length, and repeated opening verbs.

### 9. Editable LaTeX generation

Populate a reusable Times New Roman application-resume template and produce editable `.tex` source plus PDF preview when a compatible compiler is available.

## Resume modes

### Core Resume Record

Core Resume Record is an internal evidence source labeled `Not for Submission`. It preserves complete verified history, sources, technical scope, and unresolved questions. It is not optimized for a posting or page limit and must remain unchanged when creating applications.

### Application Resume

Application Resume selects only verified Core evidence for one target job. Genuine gaps remain visible instead of being filled with invented claims.

Default format:

- no Summary;
- no coursework;
- university/company left and city right;
- degree/official title on second row and dates right;
- exactly 3 bullets for every included Experience entry;
- 2-4 bullets for projects based on verified evidence;
- Skills at very end.

## Project-specific rules

- Place `Skills` at very end.
- Remove every standalone English article `a`, `an`, and `the` from resume prose.
- Never use `led`, `managed`, or `architected` in final resume content.
- Use past tense for experience and project bullets.
- Never invent metrics, tools, dates, ownership, deployments, or outcomes.
- Use verified metrics without an artificial percentage cap; add baseline, timeframe, or scope when credibility needs context.

## LaTeX template

Template: [`resume-reviewer/assets/latex/application-resume.tex`](resume-reviewer/assets/latex/application-resume.tex)

Typography and layout defaults:

- Times New Roman when installed; TeX Gyre Termes fallback;
- 18 pt name;
- 11 pt section labels;
- 10.5 pt body text;
- one-line contact block;
- ATS-readable single-column structure;
- reusable Education, Experience, Project, and bullet macros.

Compile with XeLaTeX or LuaLaTeX:

```bash
cp resume-reviewer/assets/latex/application-resume.tex application-resume.tex
xelatex application-resume.tex
```

Tectonic can also compile template:

```bash
tectonic -X compile application-resume.tex
```

Copy template before adding personal information. Keep bundled asset generic.

## Install from GitHub

### From Codex

Ask Codex:

```text
Use $skill-installer to install https://github.com/weeelin98/ResumeReviewer/tree/main/resume-reviewer
```

Skill becomes available on next turn after installation.

### With bundled installer

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo weeelin98/ResumeReviewer \
  --path resume-reviewer
```

Installer places skill at `${CODEX_HOME:-$HOME/.codex}/skills/resume-reviewer`. Existing destination must be moved or removed before reinstalling.

### Link a development checkout

Use a symbolic link when local `git pull` updates should become available without reinstalling:

```bash
git clone https://github.com/weeelin98/ResumeReviewer.git
ln -s "$(pwd)/ResumeReviewer/resume-reviewer" "${CODEX_HOME:-$HOME/.codex}/skills/resume-reviewer"
```

Create link only when destination does not already exist. Start a new Codex turn after installing or updating skill.

## Usage

Assess without rewriting:

```text
Use $resume-reviewer to diagnose ATS, credibility, evidence, and relevance problems without rewriting yet.
```

Build Core Resume Record:

```text
Use $resume-reviewer to turn my resume and raw project notes into a verified Core Resume Record for backend and AI/ML roles.
```

Build Application Resume:

```text
Use $resume-reviewer to tailor my Core Resume Record to this job description. Show requirement-to-proof map before final resume.
```

Generate LaTeX:

```text
Use $resume-reviewer to create an Application Resume from verified evidence and return editable LaTeX plus compiled PDF preview.
```

## Validate Markdown resume

```bash
python3 resume-reviewer/scripts/validate_resume.py path/to/resume.md
```

Validator supplements human review and does not validate factual accuracy.

## Repository structure

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

`resumeReviewer.json` remains a portable configuration for tools that do not load Codex skills.

## References

- Laura DeCarlo, *Resumes For Dummies*, 9th ed., John Wiley & Sons, 2026. Methodology adapted from chapters covering ATS, reverse chronology, Core and OnTarget resumes, CAR evidence, AI safeguards, resume language, new-graduate strategy, and final resume review.
- [OpenAI Developers: Codex use cases - Save workflows as skills](https://developers.openai.com/codex/use-cases). Used for Codex skill packaging direction.

This repository does not redistribute source book. Resume guidance cannot guarantee ATS ranking, interviews, or offers.
