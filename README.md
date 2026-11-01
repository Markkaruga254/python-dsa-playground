# Python & DSA Learning Path

A structured, practice-first learning path for building confidence in Python, data structures, algorithms, and technical interviews.

**Learning hub:** [Open the static course site](https://markkaruga254.github.io/python-dsa-playground/)  
**Source of truth:** this repository. Lessons, quizzes, answer keys, notes, and reference solutions are maintained as Markdown and Python files.

> **Course status:** the 16-week roadmap is planned; Week 1 is currently published. Upcoming weeks will appear on the learning hub as their lesson folders are added. A roadmap entry is not a claim that its lessons are already complete.

## Who this is for

- Learners who know basic computer use and want to learn Python and problem solving systematically.
- Students who can write simple programs but need stronger data-structure and algorithm fundamentals.
- Interview candidates who want to practise explaining, analysing, testing, and implementing solutions—not just memorising answers.

You do not need prior competitive-programming experience. The first week introduces Python fundamentals alongside simple algorithmic problems. If you are completely new to programming, work through the Python foundations at a comfortable pace before increasing the problem difficulty.

## Learning outcomes

By the end of the path, a learner should be able to:

1. Write readable Python and use core language features confidently.
2. Select and implement common data structures.
3. Recognise common problem-solving patterns and explain why they apply.
4. Analyse time and space complexity using Big-O notation.
5. Test solutions against normal, boundary, and invalid inputs.
6. Explain a solution, discuss trade-offs, and implement it independently under time constraints.

## The learning cycle

Each published session follows the same repeatable cycle:

1. **Learn:** use the linked reading or lesson to understand the concept.
2. **Trace:** work through a small example by hand before coding.
3. **Solve:** attempt the problem independently; record hints used.
4. **Analyse:** state time and space complexity and justify the data structure.
5. **Test:** cover normal cases, edge cases, and constraints.
6. **Recall:** complete the closed-book quiz before opening the answer key.
7. **Reflect:** write notes in your own words and explain the solution aloud.

Every seventh session is a **review and retention session**: revisit difficult concepts, redo selected problems from a blank file, and complete the weekly review. It is not tied to a particular weekday; learners can adapt the pace to their schedules.

See [the curriculum guide](docs/CURRICULUM.md) for the learning sequence and [the assessment guide](docs/ASSESSMENT.md) for readiness criteria.

## 16-week roadmap

| Week | Focus | Milestone |
|---|---|---|
| 1 | Python foundations, arrays, hashing | Write and explain basic Python solutions |
| 2 | Arrays and hashing, sorting, Two Pointers | Choose between sorting, sets, and dictionaries |
| 3 | Two Pointers, stacks, queues | Recognise linear-scan and stack patterns |
| 4 | Binary Search, Sliding Window | Use invariants and window boundaries correctly |
| 5 | Linked Lists | Implement pointer manipulation safely |
| 6 | Trees I | Traverse trees recursively and iteratively |
| 7 | Trees II, Tries | Apply tree properties and prefix structures |
| 8 | Heaps, Priority Queues, Backtracking | Manage ordering and explore search spaces |
| 9 | Graphs I: BFS and DFS | Model problems as graphs and traverse them |
| 10 | Graphs II: advanced graph patterns | Select graph algorithms based on constraints |
| 11 | 1-D Dynamic Programming | Define states, transitions, and base cases |
| 12 | 2-D DP, Greedy, Intervals | Compare optimisation strategies |
| 13 | Math, bit manipulation, weak-topic review | Consolidate gaps and revisit patterns |
| 14 | Timed medium problems | Solve unfamiliar problems under time limits |
| 15 | Mock technical assessments | Communicate and implement complete solutions |
| 16 | Final mocks, review, and next steps | Demonstrate independent interview-style problem solving |

The roadmap is a sequence, not a race. Revisit a topic when the weekly review shows that the fundamentals are not secure.

## Repository structure

```text
.
├── .github/
│   ├── workflows/          # Pages deployment and curriculum checks
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                   # Curriculum and assessment standards
├── resources/              # Curated learning references
├── scripts/                # Content creation and validation tools
├── templates/              # Reusable session Markdown templates
├── weeks/
│   └── week-XX/
│       ├── day-XX/
│       │   ├── plan.md
│       │   ├── quiz.md
│       │   ├── answers.md
│       │   ├── notes.md
│       │   └── solutions/
│       └── review.md
└── site/                   # Generated static navigation site
```

## Getting started

1. Read [the curriculum guide](docs/CURRICULUM.md).
2. Open the [learning hub](https://markkaruga254.github.io/python-dsa-playground/).
3. Start with the first published session: [Week 1 · Day 1](weeks/week-01/day-01/plan.md).
4. Follow the session in order and attempt the quiz before viewing its answers.
5. Record your own reasoning in `notes.md` and review your progress at the end of the week.

### Add the next session

Use the helper script to create a session from the templates:

```bash
python scripts/new_day.py 2 1
```

Then edit the generated files before committing. The script creates a scaffold; it does not write the lesson, choose appropriate problems, or validate educational quality. Follow [CONTRIBUTING.md](CONTRIBUTING.md) when adding or improving course material.

### Validate published content locally

Requires Python 3. No third-party packages are needed.

```bash
python scripts/validate_curriculum.py
python scripts/build_site.py
```

The curriculum validation runs automatically for pull requests and pushes that change course content.

## Contributing

Contributions are welcome: improve an explanation, correct an error, add a well-scoped practice session, strengthen tests, or improve accessibility and navigation.

Before opening a pull request, read [CONTRIBUTING.md](CONTRIBUTING.md). New material should be accurate, original in its explanations, accessible to the intended learner, and aligned with the assessment standards.

## Learning resources

Start with the curated [resource guide](resources/RESOURCES.md). Prefer official documentation for language behaviour and use problem platforms for practice and submission—not as substitutes for understanding.

## Project principles

- **Understanding over completion:** finishing a checklist is not the same as mastering a concept.
- **Explain the trade-off:** every solution should include a defensible complexity analysis.
- **Test deliberately:** edge cases are part of the problem, not optional polish.
- **Keep the bar consistent:** sessions use a common structure and assessment rubric.
- **Publish honestly:** planned content is labelled as planned until the actual lesson material is reviewed and merged.
