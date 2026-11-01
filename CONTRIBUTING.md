# Contributing

Thank you for helping improve the Python & DSA Learning Path. Contributions should make the material more accurate, easier to learn from, more accessible, or more maintainable.

## Ways to contribute

- Correct a technical or editorial error.
- Improve a concept explanation or worked trace.
- Add a practice session that follows the curriculum.
- Improve a solution's readability, tests, or complexity explanation.
- Improve the static learning hub, automation, or accessibility.
- Report broken links or confusing instructions.

Small, focused pull requests are easier to review than large rewrites.

## Before you start

1. Check existing files and open pull requests to avoid duplicate work.
2. For a substantial change, open an issue describing the learning problem and proposed solution first.
3. Keep the existing repository structure unless there is a clear reason to change it.
4. Do not add credentials, personal data, copied course materials, or full proprietary problem statements/editorials.

## Adding a learning session

Create the folder using:

```bash
python scripts/new_day.py <week> <day>
```

For example:

```bash
python scripts/new_day.py 2 1
```

Then replace every placeholder. The scaffold is not considered a complete lesson until the following are ready:

- `plan.md`: learning objectives, prerequisites, ordered tasks, problem links, and expected deliverables.
- `quiz.md`: at least three numbered closed-book questions.
- `answers.md`: answers with matching numbering; include reasoning for questions that test analysis.
- `notes.md`: a learner-facing reflection template, not prewritten claims about what the learner learned.
- `solutions/`: readable implementation(s), with examples or tests and complexity notes.
- Weekly `review.md`: prompts for retrieval, reflection, and the checkpoint.

Use one primary problem per session unless a second problem has a clear teaching purpose. Link to the original problem source rather than reproducing its full statement.

## Technical quality bar

A solution should:

- Use descriptive names and straightforward Python.
- State assumptions and relevant constraints.
- Handle meaningful edge cases.
- Explain why the algorithm is correct, not just what each line does.
- Include time and auxiliary-space complexity with a short justification.
- Avoid unnecessary dependencies and clever tricks that obscure the idea.

For algorithm changes, prefer tests that cover a typical input, an empty or minimal input where valid, a boundary case, and a case that would expose a common incorrect approach.

## Content quality bar

- Write explanations in your own words.
- Define new terms before relying on them.
- Use small, traceable examples.
- Distinguish a brute-force baseline from an optimised approach where useful.
- Do not label a topic mastered merely because a learner completed a task.
- Use stable, reputable references; official Python documentation is preferred for language behaviour.
- Check that external links work and point to the intended resource.

## Local checks

Run these commands before submitting:

```bash
python scripts/validate_curriculum.py
python scripts/build_site.py
python -m unittest discover -s tests -v
```

The automated validator checks the structure and basic consistency of published lessons. The Week 1 unittest suite checks behavioral correctness of the learner implementations; it is expected to fail while starter functions still contain TODO/pass. It cannot judge whether an explanation is correct or a problem is pedagogically appropriate; reviewers must still read the material.

## Pull request expectations

A pull request should explain:

- What changed.
- Why the change improves the learning experience or project.
- Which weeks/sessions are affected.
- What local checks were run.
- Any external references added or changed.

Use the pull request checklist and keep changes focused. A maintainer may request revisions where correctness, clarity, or alignment with the curriculum standards is uncertain.
