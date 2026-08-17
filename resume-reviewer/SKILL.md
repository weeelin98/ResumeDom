---
name: resume-reviewer
description: Build, review, and tailor evidence-backed US-market technology resumes for computer-science interns and new graduates. Use when Codex needs to turn raw notes or an existing resume into a verified Core Resume, tailor an application resume to a specific job description, diagnose ATS and credibility problems, extract technical evidence for frontend, backend, full-stack, AI/ML, data, infrastructure, mobile, product, or project roles, rewrite experience or project bullets, or run a final resume audit.
---

# Resume Reviewer

Create truthful, ATS-readable resume content in two distinct modes:

1. **Core Resume**: Build a complete, reusable source of verified career evidence.
2. **Application Resume**: Select and tailor Core Resume evidence for one target job description.

Explain analysis in user language. Write resume content in English unless user requests another language.

## Route Request

- Choose **Core Resume mode** when user provides raw history, an existing resume, projects, coursework, or accomplishments without one specific job posting.
- Choose **Application Resume mode** when user provides a job description or asks to tailor, target, match, or optimize a resume for one application.
- Choose **Review-only mode** when user asks for diagnosis without rewriting. Do not modify files or resume text unless requested.
- If Application Resume mode lacks a usable Core Resume, build a minimal verified evidence ledger before tailoring. Never treat target-job language as candidate experience.

## Load References

- Read [evidence-and-car.md](references/evidence-and-car.md) for Core Resume creation, fact status, CAR extraction, missing metrics, and privacy.
- Read [role-competencies.md](references/role-competencies.md) for target-role mapping and technical evidence prompts.
- Read [ats-and-layout.md](references/ats-and-layout.md) when reviewing or producing a full resume, deciding section order, or checking ATS/layout constraints.
- Read [output-schema.md](references/output-schema.md) before returning a complete diagnosis, Core Resume, or Application Resume.

## Protect Source Truth

1. Separate every claim into `VERIFIED`, `NEEDS CONFIRMATION`, or `DO NOT USE`.
2. Treat user-provided resume, notes, artifacts, and direct answers as source material. Preserve original meaning.
3. Never invent or infer employers, titles, dates, technologies, metrics, users, revenue, ownership, deployment status, or business outcomes.
4. Mark missing facts as `[NEEDS CONFIRMATION: ...]` during drafting. Remove unresolved claims from application-ready output.
5. Preserve confidential information. Use verified percentages, ranges, generalized scale, or qualitative scope when exact values cannot be disclosed.
6. Keep Core Resume unchanged when producing an Application Resume. Save or label targeted output separately.

## Enforce Project Hard Rules

Apply these rules literally to final resume content:

- Place `Skills` section at very end of resume.
- Remove every standalone English article `a`, `an`, and `the` from resume prose.
- Never use verbs `led`, `managed`, or `architected`, including capitalization variants.
- Use past tense for experience and project bullets.
- Remove first-person pronouns and filler such as `responsible for`, `proactive`, `innovative`, `passionate`, and `results-oriented`.
- Bold only selected skills and verified metrics when Markdown emphasis improves scanning. Do not bold every technology.

Do not replace forbidden verbs with stronger claims unless evidence supports ownership. Prefer precise alternatives such as `developed`, `implemented`, `built`, `optimized`, `enhanced`, `integrated`, `deployed`, `migrated`, `automated`, `coordinated`, `mentored`, or `delivered`.

## Build Core Resume

1. Collect current resume or raw history, target role family, education, work, projects, research, credentials, and relevant links.
2. Create evidence ledger using [evidence-and-car.md](references/evidence-and-car.md). Ask only high-value questions that could materially improve truth or positioning.
3. Extract Challenge, Action, Result, scope, tools, and personal contribution for each experience.
4. Map evidence to relevant role competencies using [role-competencies.md](references/role-competencies.md). Do not force evidence into unsupported categories.
5. Draft complete Core Resume without optimizing for one posting. Retain useful verified evidence even when final document exceeds one page.
6. Use reverse-chronological entries and standard section labels. Keep `Skills` last.
7. Audit truth, clarity, tense, articles, forbidden verbs, privacy, and duplicate claims.

## Build Application Resume

1. Parse target posting into title, must-haves, nice-to-haves, responsibilities, tools, outcomes, and recurring keywords.
2. Produce requirement-to-proof map with `DIRECT`, `ADJACENT`, or `GAP` status. Use only verified Core Resume evidence.
3. Mirror employer terminology only where candidate can defend wording in an interview. Spell out uncommon acronyms on first use.
4. Select strongest recent and relevant evidence. Retain unrelated work only when it proves target-relevant skills or fills chronology credibly.
5. Rewrite bullets with one of these patterns:
   - `Outcome + Action + Scope/Tools`
   - `Action + Deliverable + Scope/Quality` when no verified outcome exists
6. Use 3-5 bullets for most recent or strongest relevant experience, 1-2 for secondary experience, and 2-4 for projects. Adjust only when evidence density requires it.
7. Keep each bullet focused on one primary claim. Target roughly 18-32 words; use rendered line count rather than Markdown line wrapping as final authority.
8. Use verified metrics without numeric caps. Add baseline, timeframe, sample size, or scope when large numbers need credibility. When no metric exists, use scale, complexity, frequency, quality, delivery status, or adoption.
9. Order bullets by target relevance and proof strength. Keep reverse chronology and `Skills` at very end.
10. Identify genuine gaps instead of disguising them with keyword stuffing.

## Audit Output

Check each final draft for:

- factual traceability and unresolved placeholders;
- target-job alignment and requirement proof;
- reverse chronology, standard labels, consistent dates, and live-text essentials;
- concise bullets, useful scope, and defensible metrics;
- past tense, zero first-person voice, zero fluff, and no unsupported ownership;
- Skills section at end, zero standalone `a/an/the`, and zero `led/managed/architected`;
- privacy, confidentiality, and interview defensibility.

When resume exists as standalone Markdown, run:

```bash
python3 scripts/validate_resume.py path/to/resume.md
```

Treat script warnings as review prompts, not permission to rewrite facts. Fix only failing sections; do not restart entire workflow when one check fails.

## Interact Efficiently

Start with this compact request when inputs are missing:

> Provide current resume or raw experience, target role, and target job description if tailoring for one application. Include only facts and metrics you can defend.

Proceed with available evidence when safe. Collect unresolved questions in one short block instead of interrupting every drafting step.
