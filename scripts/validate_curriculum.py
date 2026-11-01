#!/usr/bin/env python3
"""Validate the structure and basic consistency of published course sessions."""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKS = ROOT / "weeks"
REQUIRED_SESSION_FILES = ("lesson.md", "plan.md", "quiz.md", "answers.md", "notes.md")
NUMBERED_ITEM = re.compile(r"^\s*(\d+)[.)]\s+\S", re.MULTILINE)


def numbered_items(path: Path) -> list[int]:
    return [int(match.group(1)) for match in NUMBERED_ITEM.finditer(path.read_text(encoding="utf-8"))]


def validate() -> list[str]:
    errors: list[str] = []
    if not WEEKS.exists():
        return ["weeks/ directory is missing"]

    week_dirs = sorted(WEEKS.glob("week-[0-9][0-9]"))
    if not week_dirs:
        return ["No published week directories found"]

    for week_dir in week_dirs:
        review = week_dir / "review.md"
        if not review.is_file():
            errors.append(f"{week_dir.relative_to(ROOT)}: missing review.md")

        day_dirs = sorted(week_dir.glob("day-[0-9][0-9]"))
        if not day_dirs:
            errors.append(f"{week_dir.relative_to(ROOT)}: no day directories found")
            continue

        for day_dir in day_dirs:
            relative = day_dir.relative_to(ROOT)
            for filename in REQUIRED_SESSION_FILES:
                if not (day_dir / filename).is_file():
                    errors.append(f"{relative}: missing {filename}")

            quiz = day_dir / "quiz.md"
            answers = day_dir / "answers.md"
            if quiz.is_file() and answers.is_file():
                questions = numbered_items(quiz)
                answer_items = numbered_items(answers)
                if len(questions) < 3:
                    errors.append(f"{relative}/quiz.md: expected at least 3 numbered questions")
                if questions != answer_items:
                    errors.append(
                        f"{relative}: quiz/answer numbering mismatch "
                        f"(questions={questions}, answers={answer_items})"
                    )

            solutions_dir = day_dir / "solutions"
            if not solutions_dir.is_dir():
                errors.append(f"{relative}: missing solutions/ directory")
            else:
                for solution in sorted(solutions_dir.glob("*.py")):
                    try:
                        ast.parse(solution.read_text(encoding="utf-8"), filename=str(solution))
                    except (SyntaxError, UnicodeDecodeError) as exc:
                        errors.append(f"{solution.relative_to(ROOT)}: {exc}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Curriculum validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("Curriculum structure and Python syntax checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
