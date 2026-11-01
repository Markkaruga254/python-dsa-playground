# Member Getting Started Guide

Welcome to the Python & DSA Learning Path. This guide explains how to use the learning hub, set up Python, work through the published material, and get help when something is unclear.

> **Current status:** Week 1 is published. The 16-week roadmap describes the intended sequence; later weeks are not available until their lessons are published. You can read the course site without installing anything.

## 1. Open the learning hub

Start here:

**[Open the Python & DSA Learning Hub](https://markkaruga254.github.io/python-dsa-playground/)**

The hub is a static course site for browsing lessons and navigating the curriculum. It is not an online code editor or automatic submission system. Use your own computer to write and run Python.

If you prefer reading the source files directly, start at [Week 1 · Day 1](../weeks/week-01/day-01/plan.md).

## 2. Set up Python

You need **Python 3.9 or newer** and a code editor. The Week 1 exercises and tests use Python's standard library; you do not need to install third-party Python packages.

1. Download Python from [python.org/downloads](https://www.python.org/downloads/) if it is not already installed.
2. During Windows installation, select **Add Python to PATH** if the installer offers that option.
3. Open a terminal (PowerShell or Command Prompt on Windows; Terminal on macOS or Linux).
4. Check that Python is available:

   **Windows**
   ```powershell
   py --version
   ```

   **macOS / Linux**
   ```bash
   python3 --version
   ```

   The output should show Python 3.9 or a newer version. If the command is not found, follow the installation instructions for your operating system on the official Python website.

A code editor such as [Visual Studio Code](https://code.visualstudio.com/) is useful, but any editor that can save plain-text `.py` files will work.

## 3. Get the exercise files

You can read lessons in the browser, but to edit and run the exercises you need a local copy of the repository.

First, install [Git](https://git-scm.com/downloads) if it is not already installed. Then open a terminal and run:

```bash
git clone https://github.com/Markkaruga254/python-dsa-playground.git
cd python-dsa-playground
```

If you do not want to use Git yet, you can download the repository as a ZIP from the GitHub page using **Code → Download ZIP**, then extract it.

**Keep your work separate from the course repository.** The public repository is the shared learning material. Do not push your exercise changes directly to its `main` branch. You can keep a local copy, or create your own GitHub fork if you want to save your work online. A public fork makes your work visible to others.

## 4. Work through Week 1

Follow the sessions in order:

1. Open the day's `plan.md` and complete its tasks in sequence.
2. Read `lesson.md` and trace the examples yourself.
3. Open the linked problem and attempt it before looking at any answers.
4. Implement your solution in the corresponding Python starter file.
5. Run your code and add your own test cases.
6. Answer `quiz.md` without looking at the answers, then check `answers.md`.
7. Write your reasoning, complexity analysis, and questions in `notes.md`.

Start with [Week 1 · Day 1](../weeks/week-01/day-01/plan.md). Use the [Week 1 starter-code notes](../weeks/week-01/STARTER-CODE.md) if you need more detail about the exercise files.

### Important: the files in `solutions/` are starter code

The `solutions/` folders currently contain **incomplete learner files**, not completed reference implementations. Their TODO markers and `pass` statements are intentional. Replace them with your own code.

The repository does not currently publish separate reference implementations for these Week 1 exercises. Do not assume that a file in a folder named `solutions` is already solved.

## 5. Run your code and the behavioral tests

Run an individual exercise from the repository root. For example:

**Windows**
```powershell
py weeks/week-01/day-01/solutions/contains_duplicate.py
```

**macOS / Linux**
```bash
python3 weeks/week-01/day-01/solutions/contains_duplicate.py
```

Use the equivalent Python command configured on your computer. Add your own assertions or small test cases as you work.

The repository also includes behavioral tests for the six Week 1 exercises. Run them from the repository root:

**Windows**
```powershell
py -m unittest discover -s tests -v
```

**macOS / Linux**
```bash
python3 -m unittest discover -s tests -v
```

**The tests are expected to fail while the starter functions are unfinished.** They check whether your implementations behave correctly; they do not fill in the code for you. Failures for exercises you have not implemented yet are normal. After completing an exercise, run the suite again and use the failing test name to understand which behavior still needs attention.

See [the test instructions](../tests/README.md) for the list of covered exercises and edge cases.

## 6. Track your learning

At the end of each session, make sure you can:

- Explain the approach without reading the code line by line.
- State the time and auxiliary-space complexity and justify both.
- Identify normal cases and meaningful edge cases.
- Reimplement the solution later without copying it.
- Record any hints or references you used honestly.

At the end of the week, complete the review in `weeks/week-01/review.md`. Use the [assessment guide](ASSESSMENT.md) to judge your progress. Understanding matters more than finishing every task quickly.

## 7. Ask for help or report a problem

For a broken link, unclear instruction, suspected content error, or repository issue, use [GitHub Issues](https://github.com/Markkaruga254/python-dsa-playground/issues). Issues are public, so do not include passwords, access tokens, private information, or anything you do not want visible.

When reporting a problem, include:

- The file or lesson name (and the day, if relevant).
- What you expected to happen and what happened instead.
- Your operating system and Python version, if it is a coding issue.
- The exact command you ran and the relevant error output.

For questions about a GDG session, deadlines, or cohort coordination, use the communication channel announced by the GDG organisers. This repository does not define a separate assignment-submission or private code-review process.

## Quick start checklist

- [ ] Open the [learning hub](https://markkaruga254.github.io/python-dsa-playground/).
- [ ] Install Python 3.9+ and confirm the version in your terminal.
- [ ] Download or clone the repository.
- [ ] Start with [Week 1 · Day 1](../weeks/week-01/day-01/plan.md).
- [ ] Attempt the problem before checking the quiz answers.
- [ ] Implement the TODO in the starter file and run your own tests.
- [ ] Keep your work separate from the shared course repository.
