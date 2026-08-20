---
name: resume-reviewer
description: Build, assess, review, and tailor evidence-backed US-market technology resumes for computer-science interns and new graduates. Use when Codex needs to turn raw notes or an existing resume into a verified Core Resume Record, tailor an Application Resume to a specific job description, diagnose ATS and credibility problems, extract technical evidence for frontend, backend, full-stack, AI/ML, data, infrastructure, mobile, product, or project roles, rewrite experience or project bullets, generate an editable LaTeX resume, or run a final resume audit.
---

# Resume Reviewer

Create truthful, ATS-readable resume content in two distinct modes:

1. **Core Resume Record**: Maintain an internal, complete record of verified career evidence. Treat it as source data only, never as a submission document.
2. **Application Resume**: Select and tailor Core Resume evidence for one target job description.

Explain analysis in user language. Write resume content in English unless user requests another language.

## Route Request

- Choose **Core Resume mode** when user provides raw history, an existing resume, projects, coursework, or accomplishments without one specific job posting.
- Choose **Application Resume mode** when user provides a job description or asks to tailor, target, match, or optimize a resume for one application.
- Choose **Review-only mode** when user asks for diagnosis without rewriting. Do not modify files or resume text unless requested.
- If Application Resume mode lacks a usable Core Resume, build a minimal verified evidence ledger before tailoring. Never treat target-job language as candidate experience.
- Choose **LaTeX output** when user asks for editable source, PDF rendering, or template-based formatting. Use only verified Application Resume content.

## Load References

- Read [evidence-and-car.md](references/evidence-and-car.md) for Core Resume creation, fact status, CAR extraction, missing metrics, and privacy.
- Read [role-competencies.md](references/role-competencies.md) for target-role mapping and technical evidence prompts.
- Read [ats-and-layout.md](references/ats-and-layout.md) when reviewing or producing a full resume, deciding section order, or checking ATS/layout constraints.
- Read [resume-templates.md](references/resume-templates.md) before producing a Core Resume Record or Application Resume.
- Read [output-schema.md](references/output-schema.md) before returning a complete diagnosis, Core Resume, or Application Resume.

## Protect Source Truth

1. Separate every claim into `VERIFIED`, `NEEDS CONFIRMATION`, or `DO NOT USE`.
2. Treat user-provided resume, notes, artifacts, and direct answers as source material. Preserve original meaning.
3. Never invent or infer employers, titles, dates, technologies, metrics, users, revenue, ownership, deployment status, or business outcomes.
4. Mark missing facts as `[NEEDS CONFIRMATION: ...]` during drafting. Remove unresolved claims from application-ready output.
5. Preserve confidential information. Use verified percentages, ranges, generalized scale, or qualitative scope when exact values cannot be disclosed.
6. Use Core Resume only as an internal factual record. Do not optimize it for one posting, present it as submission-ready, or replace source facts with polished claims.
7. Keep Core Resume unchanged when producing an Application Resume. Save or label targeted output separately.

## Enforce Project Hard Rules

Apply these rules literally to final resume content:

- Place `Skills` section at very end of resume.
- Remove every standalone English article `a`, `an`, and `the` from resume prose.
- Never use verbs `led`, `managed`, or `architected`, including capitalization variants.
- Use past tense for experience and project bullets.
- Remove first-person pronouns and filler such as `responsible for`, `proactive`, `innovative`, `passionate`, and `results-oriented`.
- Bold only selected skills and verified metrics when Markdown emphasis improves scanning. Do not bold every technology.

Do not replace forbidden verbs with stronger claims unless evidence supports ownership. Prefer precise alternatives such as `developed`, `implemented`, `built`, `optimized`, `enhanced`, `integrated`, `deployed`, `migrated`, `automated`, `coordinated`, `mentored`, or `delivered`.

## Build Core Resume Record

1. Collect current resume or raw history, target role family, education, work, projects, research, credentials, and relevant links.
2. Create evidence ledger using [evidence-and-car.md](references/evidence-and-car.md). Ask only high-value questions that could materially improve truth or positioning.
3. Extract Challenge, Action, Result, scope, tools, and personal contribution for each experience.
4. Map evidence to relevant role competencies using [role-competencies.md](references/role-competencies.md). Do not force evidence into unsupported categories.
5. Record complete verified evidence without optimizing for one posting. Preserve source, status, factual scope, and unresolved questions. Allow document to exceed one page.
6. Label output `Core Resume Record - Not for Submission`. Do not treat polish, brevity, keyword density, or page count as goals.
7. Use reverse-chronological entries and standard section labels. Keep `Skills` last.
8. Audit truth, source traceability, privacy, and duplicate claims. Preserve `NEEDS CONFIRMATION` labels until user verifies facts.

## Build Application Resume

1. Parse target posting into title, must-haves, nice-to-haves, responsibilities, tools, outcomes, and recurring keywords.
2. Produce requirement-to-proof map with `DIRECT`, `ADJACENT`, or `GAP` status. Use only verified Core Resume evidence.
3. Mirror employer terminology only where candidate can defend wording in an interview. Spell out uncommon acronyms on first use.
4. Select strongest recent and relevant evidence. Retain unrelated work only when it proves target-relevant skills or fills chronology credibly.
5. Rewrite bullets with one of these patterns:
   - `Outcome + Action + Scope/Tools`
   - `Action + Deliverable + Scope/Quality` when no verified outcome exists
6. Omit Summary and coursework. Format Education as university left with city right, followed by degree left with dates right.
7. Format each Experience entry as company left with city right, followed by official job title left with dates right.
8. Use exactly 3 bullets for every included Experience entry. Use 2-4 bullets for projects based on relevant verified evidence.
9. Keep each bullet focused on one primary claim. Target roughly 18-32 words; use rendered line count rather than Markdown line wrapping as final authority.
10. Use verified metrics without numeric caps. Add baseline, timeframe, sample size, or scope when large numbers need credibility. When no metric exists, use scale, complexity, frequency, quality, delivery status, or adoption.
11. Order bullets by target relevance and proof strength. Keep reverse chronology and `Skills` at very end.
12. Identify genuine gaps instead of disguising them with keyword stuffing.

## Generate LaTeX Resume

1. Copy [application-resume.tex](assets/latex/application-resume.tex) into user output location. Never overwrite bundled asset with candidate information.
2. Replace placeholders with verified Application Resume content only. Remove unused entries and optional fields.
3. Preserve default typography unless user requests another format: Times New Roman, 18 pt name, 11 pt section labels, and 10.5 pt body text.
4. Keep contact information on one line when it fits. Keep Education and Experience two-row alignment and Skills at end.
5. Escape LaTeX special characters in user content, links, employer names, and project names.
6. Compile with XeLaTeX or LuaLaTeX. Tectonic is acceptable when it uses XeTeX-compatible font handling.
7. Render and inspect final PDF for clipping, overflow, page count, line wrapping, spacing, and live text. Deliver editable `.tex` plus PDF preview when compilation is available.

## Audit Output

Check each final draft for:

- factual traceability and unresolved placeholders;
- target-job alignment and requirement proof;
- reverse chronology, standard labels, consistent dates, and live-text essentials;
- no Summary or coursework in Application Resume;
- correct left/right entry hierarchy and exactly 3 bullets per included Experience entry;
- concise bullets, useful scope, and defensible metrics;
- past tense, zero first-person voice, zero fluff, and no unsupported ownership;
- Skills section at end, zero standalone `a/an/the`, and zero `led/managed/architected`;
- privacy, confidentiality, and interview defensibility.

For LaTeX output, also check compilation warnings, embedded font, one-line contact alignment, and PDF text extraction.

When resume exists as standalone Markdown, run:

```bash
python3 scripts/validate_resume.py path/to/resume.md
```

Treat script warnings as review prompts, not permission to rewrite facts. Fix only failing sections; do not restart entire workflow when one check fails.

## Interact Efficiently

Start with this compact request when inputs are missing:

> Provide current resume or raw experience, target role, and target job description if tailoring for one application. Include only facts and metrics you can defend.

Proceed with available evidence when safe. Collect unresolved questions in one short block instead of interrupting every drafting step.
