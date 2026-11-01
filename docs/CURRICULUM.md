# Curriculum guide

## Purpose

This course develops practical Python fluency and transferable problem-solving skills for data-structure, algorithm, and technical-interview problems. It is designed around deliberate practice: understand a concept, trace it, implement it, analyse it, test it, and explain it.

The roadmap spans 16 weeks. The published learning hub only displays sessions that exist in the repository; planned topics are not presented as completed lessons.

## Intended learner

The path is suitable for:

- Beginners who are learning Python while building algorithmic foundations.
- Students who know basic programming constructs and want a structured DSA sequence.
- Interview candidates who need to improve implementation, analysis, and communication.

A learner should be comfortable using a computer, editing files, running Python, and reading basic instructions. Week 1 introduces core Python concepts. Learners with no programming experience should take additional time rather than treating the calendar as a deadline.

## Learning outcomes

Learners should progressively be able to:

1. Write clear Python functions and use built-in collections appropriately.
2. Translate a problem statement into inputs, outputs, constraints, and examples.
3. Choose suitable data structures and explain the choice.
4. Recognise common patterns such as hashing, two pointers, sliding windows, traversal, and dynamic programming.
5. Analyse time and auxiliary-space complexity.
6. Test normal cases, boundary conditions, and relevant edge cases.
7. Compare a straightforward solution with a more efficient alternative.
8. Communicate a correct solution and its trade-offs without relying on memorised code.

## Session design

A standard learning session should contain:

1. **Concept:** a concise explanation with prerequisites and vocabulary.
2. **Worked trace:** a small example showing how the algorithm changes state.
3. **Practice:** one primary problem and, where appropriate, one extension problem. Link to the original problem rather than copying proprietary problem statements.
4. **Implementation:** a solution file with a clear function, meaningful names, and representative tests or examples.
5. **Complexity:** time and auxiliary-space analysis, including the reasoning behind the result.
6. **Quiz:** at least three closed-book questions that test understanding, not just recall.
7. **Answer key:** numbered answers matching the quiz, with explanations where a misconception is likely.
8. **Reflection:** learner notes on what was understood, what was difficult, and what should be revisited.

Not every session needs two problems. One well-understood problem is better than several copied solutions.

## Weekly rhythm

Sessions 1–6 introduce and practise new material. Session 7 is reserved for retrieval and consolidation:

- Revisit the hardest concepts from the week.
- Redo up to three representative problems from a blank file, without looking at previous solutions.
- Explain the approach and complexity aloud.
- Complete a short weekly assessment.
- Record topics that need another pass before moving on.

The rhythm is intentionally independent of weekdays. Learners can spread sessions across their own schedules without making a review day fall on a particular date.

## Roadmap and checkpoints

| Week | Topics | Expected checkpoint |
|---|---|---|
| 1 | Python foundations, arrays, hashing | Write basic functions; use lists, sets, and dictionaries; explain a brute-force baseline |
| 2 | Arrays and hashing, sorting, Two Pointers | Compare sorting and hashing; reason about pointer movement |
| 3 | Two Pointers, stacks, queues | Identify when a stack or queue models the problem |
| 4 | Binary Search, Sliding Window | Maintain search and window invariants; handle boundaries |
| 5 | Linked Lists | Trace references and implement common pointer operations |
| 6 | Trees I | Explain tree terminology and implement DFS/BFS traversals |
| 7 | Trees II, Tries | Apply tree properties and prefix-based lookup |
| 8 | Heaps, Priority Queues, Backtracking | Use priority queues and structure recursive search |
| 9 | Graphs I: BFS and DFS | Represent graphs and reason about visited state |
| 10 | Graphs II | Select suitable graph algorithms for weighted and unweighted problems |
| 11 | 1-D Dynamic Programming | Define state, transition, base case, and iteration order |
| 12 | 2-D DP, Greedy, Intervals | Compare greedy choices with DP and interval strategies |
| 13 | Math, bit manipulation, review | Strengthen weak areas and explain common bit operations |
| 14 | Timed medium problems | Manage time while preserving correctness and communication |
| 15 | Mock technical assessments | Complete interview-style problem-solving sessions |
| 16 | Final mocks and consolidation | Demonstrate independent problem solving and identify next steps |

These are topic-level milestones, not a promise that every listed session has already been authored.

## Teaching and content standards

- Explain why an approach works; do not only show code.
- Introduce a simple baseline before presenting an optimisation when that comparison is educational.
- State assumptions and input constraints.
- Use Pythonic, readable code without hiding the algorithm behind clever one-liners.
- Distinguish average-case, worst-case, and amortised complexity when relevant.
- Explain auxiliary space separately from input storage where useful.
- Use examples that include edge cases.
- Link to authoritative documentation and reputable learning resources.
- Review external links periodically; mark unavailable resources for replacement.
- Do not reproduce full proprietary problem statements, editorials, or course content. Link to the source and write original explanations.

## Mastery is demonstrated, not assumed

A learner should be able to solve a representative problem again after a delay, explain the algorithm without reading notes, analyse complexity, and test edge cases. A completed checklist or green submission alone is not evidence of mastery. See [the assessment guide](ASSESSMENT.md).
