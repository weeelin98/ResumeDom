# Output Schema

## Diagnosis or Review

Return sections in this order:

1. **Verdict**: concise assessment of target fit and largest risks.
2. **Diagnosis**: ATS, relevance, evidence, wording, credibility, and layout findings.
3. **Evidence gaps**: facts required before stronger rewrite.
4. **Recommended changes**: prioritized actions without silently rewriting when user requested review only.

## Core Resume Mode

Return:

1. **Input status**: verified sources, assumptions, and missing facts.
2. **Evidence ledger**: compact `Claim | Status | Source | Missing detail` table.
3. **Core competency inventory**: verified evidence grouped by role family.
4. **Core Resume Record**: complete internal factual record labeled `Not for Submission`, with sources, status, unresolved questions, and Skills last.
5. **Questions**: short list of missing facts with highest expected value.
6. **Audit**: truth, privacy, grammar, project hard rules, and unresolved placeholders.

Do not trim Core Resume only to satisfy one-page application length. Do not present it as polished or application-ready.

## Application Resume Mode

Return:

1. **Target summary**: role, employer, and main hiring priorities.
2. **Requirement-to-proof map**:

| Requirement | Priority | Candidate proof | Match | Resume action |
|---|---|---|---|---|
| Job requirement | Must/Nice | Verified source or none | DIRECT/ADJACENT/GAP | Keep, reword, ask, or omit |

3. **Missing facts**: questions that could change candidacy or wording.
4. **Application Resume draft**: targeted Markdown using Core Resume evidence, no Summary, no coursework, required entry alignment, exactly 3 bullets per Experience entry, reverse chronology, and Skills last.
5. **LaTeX package when requested**: editable `.tex` populated from bundled template plus compiled PDF preview when compatible tooling is available.
6. **Change rationale**: major selections, removals, and terminology changes.
7. **Final audit**: ATS, target alignment, factual traceability, privacy, line focus, articles, forbidden verbs, Skills placement, and LaTeX compilation/rendering when applicable.

## Final-Ready Behavior

- Remove all unresolved placeholders from application-ready output.
- Separate diagnosis from resume text so user can copy resume cleanly.
- Never present match score as objective ATS prediction. Describe evidence coverage instead.
- State genuine gaps plainly; do not fabricate filler to close them.
- Keep bundled LaTeX asset generic. Copy it before inserting candidate information.
