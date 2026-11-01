# Day 03 — Booleans, conditionals, linear search, and Two Sum

## Learning goals

Evaluate Boolean expressions, understand truthiness, trace a linear scan, and implement a correct brute-force solution to Two Sum.

## 1. Boolean expressions and truthiness

Comparisons produce Boolean values: True or False. The operators and, or, and not combine or invert conditions.

    3 > 2 and 5 < 4  # False
    bool("")         # False
    bool([])         # False
    bool(0)          # False

Empty strings, empty collections, numeric zero, and None are falsey. Most other values are truthy. Therefore, if items is a concise way to check whether a list is non-empty.

## 2. Linear search

Linear search checks values one by one until it finds a match or reaches the end.

    def find_index(nums, target):
        for index, value in enumerate(nums):
            if value == target:
                return index
        return -1

Best case: O(1), when the first item matches. Worst case: O(n), when the target is last or absent. The loop uses O(1) auxiliary space.

## 3. Two Sum: brute force first

Given a list and a target, return the indices of two distinct elements whose values add to the target. Assume the problem guarantees exactly one solution unless the prompt says otherwise.

    def two_sum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

The inner loop begins at i + 1 because an element cannot pair with itself, and each unordered pair only needs to be checked once.

## Worked trace

For nums = [2, 7, 11, 15] and target = 9, start at index 0 (value 2), compare with index 1 (value 7), and return [0, 1] because their sum is 9.

The worst-case time is O(n²), and auxiliary space is O(1). The next session uses a dictionary to reduce the expected running time.

## Check your understanding

Trace the loops for [3, 2, 4] with target 6. Explain why the returned values are indices rather than the numbers themselves.

**Practice:** complete the Boolean and conditional exercises, then implement the brute-force version. The file in solutions/ is starter code.
