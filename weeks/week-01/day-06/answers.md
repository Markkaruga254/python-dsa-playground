# Day 06 Answers

Only open this after you have attempted the quiz.

1. "ell"

2. 2

3. 0

4. A list cannot be a dictionary key because it is unhashable. A tuple can be a key only if all of its elements are hashable.

5. Use the sorted letters, such as "".join(sorted(word)), or a tuple of 26 letter counts under the lowercase-English constraint. Sorting costs O(k log k) per word; counting costs O(k) per word for a fixed alphabet. For n words of max length k, totals are O(n·k log k) or O(n·k), respectively.
