# Week 1 exercise tests

Run the behavioral test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests cover the six Week 1 Python exercises:

- Contains Duplicate
- Valid Anagram
- Two Sum (brute force and hash map)
- Valid Palindrome
- Group Anagrams

They check ordinary examples and edge cases such as empty inputs, repeated values, negative numbers, punctuation, repeated characters, and valid index pairs.

## Important: starter code is intentionally incomplete

The exercise files still contain TODO/pass. Therefore, the test suite is expected to report failures until you implement the functions. That is intentional: the tests are a correctness check for your implementation, not a substitute for it.

Work through one exercise at a time. After implementing a function, run the full suite again. Failures in exercises you have not reached yet are expected; use the test name to identify the behavior you need to support.

The suite uses only Python's standard library, so no third-party test dependency is required. The CI workflow does not run these behavioral tests yet because the published exercise files are learner starter code and are not complete reference implementations.
