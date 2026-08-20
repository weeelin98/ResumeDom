# Resume Templates

## Core Resume Record

Use Core Resume only as internal source record. Label it `Core Resume Record - Not for Submission`. Preserve verified facts, sources, dates, technologies, scope, and fuller evidence inventory. Keep unresolved claims marked `NEEDS CONFIRMATION`. Do not tailor it to any posting or treat page count as constraint.

```markdown
# [FULL NAME]

[City, State] | [Email] | [Phone]
[LinkedIn] | [GitHub] | [Portfolio]

## EDUCATION

[University Name]                                      [City, State / Country]
[Degree, Major or Track]                               [Month Year - Month Year]

## EXPERIENCE

[Company Name]                                         [City, State / Country]
[Official Job Title]                                   [Month Year - Month Year]

- [Verified factual contribution, technology, scope, and source status]
- [Verified factual contribution, technology, scope, and source status]
- [NEEDS CONFIRMATION: unresolved detail]

## PROJECTS

[Project Name]                                         [Month Year - Month Year]
[Technology Stack] | [Repository or Demo]

- [Verified factual contribution and source]
- [Verified factual contribution and source]

## RESEARCH / PUBLICATIONS / AWARDS

[Include only sections supported by source material]

## SKILLS

Languages: [Verified languages]
Frameworks and AI/ML: [Verified frameworks, libraries, and methods]
Backend and Data: [Verified APIs, databases, and data systems]
Tools and Platforms: [Verified tools and platforms]
```

## Application Resume

Do not include Summary or coursework. Select only verified evidence relevant to target posting. Remove all unresolved placeholders before delivery.

```markdown
# [FULL NAME]

[City, State] | [Email] | [Phone]
[LinkedIn] | [GitHub] | [Portfolio]

## EDUCATION

[University Name]                                      [City, State / Country]
[Degree, Major or Track]                               [Month Year - Month Year]

## EXPERIENCE

[Company Name]                                         [City, State / Country]
[Official Job Title]                                   [Month Year - Month Year]

- [Target-relevant verified action, technology, and impact]
- [Target-relevant verified action, technology, and impact]
- [Target-relevant verified action, technology, and impact]

## PROJECTS

[Project Name]                                         [Month Year - Month Year]
[Technology Stack] | [Optional Repository or Demo]

- [Target-relevant verified action, technology, and impact]
- [Target-relevant verified action, technology, and impact]
- [Target-relevant verified action, technology, and impact]

## SKILLS

Languages: [Verified target-relevant languages]
Frameworks and AI/ML: [Verified target-relevant technologies]
Backend and Data: [Verified target-relevant technologies]
Tools and Platforms: [Verified target-relevant tools and platforms]
```

## Layout Rules

- Keep all essential text in normal document body.
- Use standard section labels and reverse chronology.
- Use Education and Experience two-row alignment exactly as shown.
- Use exactly 3 bullets for every included Experience entry.
- Keep Skills at end.
- Remove unused optional links and sections.

## LaTeX Asset

Use [application-resume.tex](../assets/latex/application-resume.tex) when user requests editable LaTeX or PDF rendering. Copy asset to output location before inserting candidate information. Do not modify bundled asset with personal data.

Template defaults match project Application Resume format:

- Times New Roman when installed, with TeX Gyre Termes fallback;
- 18 pt name, 11 pt section labels, and 10.5 pt body text;
- one-line contact information;
- university/company left with city right;
- degree/title left with dates right;
- exactly 3 bullets per Experience entry;
- Skills at end.

Compile with XeLaTeX, LuaLaTeX, or Tectonic. Inspect rendered PDF before delivery.
