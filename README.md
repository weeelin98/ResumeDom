# ResumeReviewer

<p align="center">
  <b>English</b> ·
  <a href="README.zh-CN.md">简体中文</a>
</p>

ResumeReviewer is a Codex skill for truthful, ATS-readable US technology resumes for computer-science interns and new graduates. It separates reusable career evidence from job-specific application content.

## Two resume modes

### 1. Core Resume

Build a complete source of verified career facts, CAR stories, projects, technical scope, and accomplishments. Core Resume is not tied to one posting and should remain unchanged when creating applications.

### 2. Application Resume

Analyze one job description, map requirements to verified Core Resume evidence, select strongest proof, and create a targeted reverse-chronological resume. Genuine gaps remain visible instead of being filled with invented claims.

## Project-specific rules

- Place `Skills` at very end.
- Remove every standalone English article `a`, `an`, and `the` from resume prose.
- Never use `led`, `managed`, or `architected` in final resume content.
- Use past tense for experience and project bullets.
- Never invent metrics, tools, dates, ownership, deployments, or outcomes.
- Use verified metrics without an artificial percentage cap; add baseline, timeframe, or scope when credibility needs context.

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

Use a symbolic link when you want local `git pull` updates to become available without reinstalling:

```bash
git clone https://github.com/weeelin98/ResumeReviewer.git
ln -s "$(pwd)/ResumeReviewer/resume-reviewer" "${CODEX_HOME:-$HOME/.codex}/skills/resume-reviewer"
```

Create link only when destination does not already exist. Start a new Codex turn after installing or updating skill.

## Usage

Build Core Resume:

```text
Use $resume-reviewer to turn my resume and raw project notes into a verified Core Resume for backend and AI/ML roles.
```

Build application resume:

```text
Use $resume-reviewer to tailor my Core Resume to this job description. Show requirement-to-proof map before final resume.
```

Review only:

```text
Use $resume-reviewer to diagnose ATS, credibility, and relevance problems without rewriting yet.
```

## Validate Markdown resume

```bash
python3 resume-reviewer/scripts/validate_resume.py path/to/resume.md
```

Validator checks Skills placement, articles, forbidden verbs, first-person language, filler, unresolved placeholders, bullet length, and repeated opening verbs. It supplements human review and does not validate factual accuracy.

## Repository structure

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

`resumeReviewer.json` remains a portable configuration for tools that do not load Codex skills.

## References

- Laura DeCarlo, *Resumes For Dummies*, 9th ed., John Wiley & Sons, 2026. Methodology adapted from chapters covering ATS, reverse chronology, Core and OnTarget resumes, CAR evidence, AI safeguards, resume language, new-graduate strategy, and final resume review.
- [OpenAI Developers: Codex use cases - Save workflows as skills](https://developers.openai.com/codex/use-cases). Used for Codex skill packaging direction.

This repository does not redistribute source book. Resume guidance cannot guarantee ATS ranking, interviews, or offers.
