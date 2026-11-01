# Day 01 — Python foundations and algorithms

## Learning goals

Read simple Python expressions, distinguish integers from floats, use arithmetic operators, and describe an algorithm as a finite sequence of steps.

## 1. Python values and expressions

Common Python types include int (whole numbers), float (decimal numbers), str (text), and bool (True or False). Use type(value) to inspect a value.

    print(type(3))       # int
    print(type(3.0))     # float
    print(7 // 2)        # 3: floor division
    print(7 % 2)         # 1: remainder

The // and % operators are useful when reasoning about integer division, parity, and grouping.

## 2. What is an algorithm?

An algorithm is a finite, unambiguous sequence of steps that transforms input into the required output. A good solution is not just code that happens to work: it has a reasoned approach, handles relevant edge cases, and has understandable performance.

For a list [4, 1, 7], a simple algorithm to find the largest value is:

1. Assume the first value is the largest seen so far.
2. Visit each remaining value.
3. Replace the current largest when a larger value appears.
4. Return the largest value.

This examines each item once, so its running time grows linearly with the list length: O(n).

## 3. Contains Duplicate: begin with a baseline

The problem asks whether any value appears at least twice. A direct baseline compares each item with the items after it:

    def contains_duplicate_brute_force(nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

For n distinct items, the maximum number of pair comparisons is n(n - 1) / 2. That grows proportionally to n squared, so the time complexity is O(n²). The algorithm uses O(1) auxiliary space because it does not build another collection.

A later session introduces a set-based approach. Do not skip the baseline: being able to explain a simple correct approach makes optimisation easier to reason about.

## Worked trace

For [2, 5, 2], compare index 0 with index 1 (no match), then index 0 with index 2 (match), and return True. For [2, 5, 7], no pair matches, so return False.

## Check your understanding

Explain why the inner loop starts at i + 1, and why the algorithm's worst-case time is quadratic.

**Practice:** complete the linked Python exercises, then attempt Contains Duplicate without looking at an editorial. The file in solutions/ is starter code; replace its TODO with your implementation.
