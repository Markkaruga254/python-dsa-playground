# Day 05 — Loops, sets, and Valid Palindrome

## Learning goals

Choose between for and while, use a set for membership checks, and understand the two-pointer strategy for palindrome checking.

## 1. Loops

Use a for loop when iterating over a known sequence or range. Use a while loop when repetition is controlled by a condition that is checked before each iteration.

    for value in [2, 4, 6]:
        print(value)

    remaining = 3
    while remaining > 0:
        remaining -= 1

A while loop must make progress toward a condition that eventually becomes false; otherwise, it can run forever.

## 2. Sets and membership

A set stores unique hashable values. Adding an existing value does not create a duplicate. Membership checks such as value in seen are O(1) on average.

    def contains_duplicate(nums):
        seen = set()
        for number in nums:
            if number in seen:
                return True
            seen.add(number)
        return False

Expected time is O(n) and auxiliary space is O(n). This improves on the O(n²) pair-comparison baseline by using extra memory.

## 3. Valid Palindrome

A palindrome reads the same forward and backward after ignoring non-alphanumeric characters and letter case. For example, "A man, a plan, a canal: Panama" is a palindrome.

One approach builds a cleaned string:

    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

This is O(n) time and O(n) additional space.

A two-pointer approach avoids building the cleaned string:
1. Put one pointer at the left end and one at the right end.
2. Move either pointer inward while it points at a non-alphanumeric character.
3. Compare the lowercase forms of the two characters.
4. If they differ, return False; otherwise move both pointers inward.
5. If the pointers meet or cross, return True.

This is O(n) time and O(1) auxiliary space.

## Worked trace

For "race a car", ignore the spaces. Compare r with r, then a with a, then c with a. The mismatch means the string is not a palindrome. For a string containing only spaces, there are no alphanumeric characters to contradict the palindrome condition, so the result is True.

## Check your understanding

Explain what str.isalnum() checks, and why moving the pointers past punctuation does not change the required comparison.

**Practice:** implement a cleaned-string version first; if comfortable, implement the two-pointer version. The file in solutions/ is starter code.
