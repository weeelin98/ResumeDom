#!/usr/bin/env python3
"""Lint standalone Markdown resumes against ResumeReviewer project rules."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


ARTICLE_RE = re.compile(r"\b(?:a|an|the)\b", re.IGNORECASE)
FORBIDDEN_RE = re.compile(r"\b(?:led|managed|architected)\b", re.IGNORECASE)
FIRST_PERSON_RE = re.compile(r"\b(?:I|me|my|mine|we|our|ours)\b", re.IGNORECASE)
FILLER_RE = re.compile(
    r"\b(?:responsible for|results-oriented|proactive|innovative|passionate)\b",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(r"\[(?:NEEDS CONFIRMATION|需要确认)(?::[^\]]+)?\]", re.IGNORECASE)
BULLET_RE = re.compile(r"^\s*[-*+]\s+(.*\S)\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
WORD_RE = re.compile(r"\b[\w+#./%-]+\b")
INITIAL_VERB_RE = re.compile(r"^(?:\*\*|__)?([A-Za-z][A-Za-z-]+)")


def strip_markdown(text: str) -> str:
    text = re.sub(r"`[^`]*`", "", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*_~]", "", text)


def lint(path: Path) -> tuple[list[str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    warnings: list[str] = []
    headings: list[tuple[int, int, str]] = []
    initial_verbs: list[tuple[int, str]] = []
    in_fence = False

    for number, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not raw.strip():
            continue

        heading = HEADING_RE.match(raw)
        if heading:
            headings.append((number, len(heading.group(1)), strip_markdown(heading.group(2)).strip()))
            continue

        bullet = BULLET_RE.match(raw)
        content = bullet.group(1) if bullet else raw.strip()
        plain = strip_markdown(content)

        for match in ARTICLE_RE.finditer(plain):
            errors.append(f"line {number}: standalone article '{match.group(0)}'")
        for match in FORBIDDEN_RE.finditer(plain):
            errors.append(f"line {number}: forbidden verb '{match.group(0)}'")
        if FIRST_PERSON_RE.search(plain):
            errors.append(f"line {number}: first-person pronoun")
        if FILLER_RE.search(plain):
            errors.append(f"line {number}: filler phrase '{FILLER_RE.search(plain).group(0)}'")
        if PLACEHOLDER_RE.search(plain):
            errors.append(f"line {number}: unresolved confirmation placeholder")

        if bullet:
            word_count = len(WORD_RE.findall(plain))
            if word_count > 32:
                warnings.append(f"line {number}: long bullet ({word_count} words; target <= 32)")
            if word_count < 8:
                warnings.append(f"line {number}: short bullet ({word_count} words); verify action and value")
            verb = INITIAL_VERB_RE.match(content.strip())
            if verb:
                initial_verbs.append((number, verb.group(1).lower()))

    skills = [item for item in headings if item[2].strip().lower() in {"skills", "technical skills"}]
    if not skills:
        errors.append("missing Skills section")
    else:
        skills_line, skills_level, _ = skills[-1]
        later_same_or_higher = [
            item for item in headings if item[0] > skills_line and item[1] <= skills_level
        ]
        if later_same_or_higher:
            errors.append(
                f"line {skills_line}: Skills section is not final section; "
                f"followed by '{later_same_or_higher[0][2]}'"
            )

    counts = Counter(verb for _, verb in initial_verbs)
    for verb, count in sorted(counts.items()):
        if count >= 3:
            line_numbers = [str(number) for number, item in initial_verbs if item == verb]
            warnings.append(f"repeated opening verb '{verb}' on lines {', '.join(line_numbers)}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resume", type=Path, help="Standalone Markdown resume")
    args = parser.parse_args()

    if not args.resume.is_file():
        print(f"ERROR: file not found: {args.resume}", file=sys.stderr)
        return 2

    errors, warnings = lint(args.resume)
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
