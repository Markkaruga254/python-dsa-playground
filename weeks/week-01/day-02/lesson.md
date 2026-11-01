# Day 02 — Functions, lists, and anagrams

## Learning goals

Write a function with parameters and a return value, use positive and negative list indexes, and compare two strategies for checking whether strings are anagrams.

## 1. Functions: inputs, work, outputs

A function gives a reusable name to a block of logic. Parameters receive input; return sends a result back to the caller.

    def square(x):
        return x * x

    result = square(4)  # 16

A function that reaches its end without executing return returns None. Calling print inside a function is not the same as returning a value: printing displays something, while returning makes a value available to the caller. Use help(len) to inspect built-in documentation.

## 2. Lists and indexing

Lists are ordered, mutable sequences. Indexing starts at zero:

    items = ["red", "green", "blue"]
    items[0]   # "red"
    items[-1]  # "blue"
    items[1:3] # ["green", "blue"]

A slice includes its start index and excludes its stop index. This half-open convention is common throughout Python.

## 3. Valid Anagram

Two strings are anagrams when they contain the same characters with the same frequencies, regardless of order. For example, "anagram" and "nagaram" are anagrams; "rat" and "car" are not.

**Approach A — sort and compare**

    def is_anagram_sort(s, t):
        return sorted(s) == sorted(t)

Sorting places equal characters in the same order. For strings of length n, sorting is O(n log n) time. The sorted lists require O(n) additional space.

**Approach B — count characters**

Count how often each character occurs in each string, then compare the counts. A dictionary can store the frequencies. This takes O(n) expected time for a fixed or suitably bounded character domain, with O(k) space for k distinct characters. Python's collections.Counter can perform this counting.

Always check lengths first: strings of different lengths cannot be anagrams.

## Worked trace

For s = "aab" and t = "aba", both frequency maps are {"a": 2, "b": 1}, so the strings are anagrams. For "a" and "ab", the lengths differ, so return False immediately.

## Check your understanding

Explain why counting frequencies avoids sorting, and identify when sorting may still be a reasonable, simpler choice.

**Practice:** finish the linked Python exercises, then implement Valid Anagram using sorting first. If time permits, implement the frequency-count approach as a second version. The file in solutions/ is starter code.
