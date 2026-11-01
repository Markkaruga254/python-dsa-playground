# Day 04 — Lists, hash maps, and the faster Two Sum

## Learning goals

Use list operations and slices, understand dictionary key/value pairs, and explain the trade-off between brute force and a hash map.

## 1. List operations

Lists are mutable. append(x) adds one item to the end of the existing list. Slicing creates a new list containing the selected range:

    nums = [10, 20, 30, 40]
    nums.append(50)
    nums[1:3]  # [20, 30]

A slice's stop index is excluded.

## 2. Hash maps (Python dictionaries)

A dictionary stores key/value pairs. A key is used to find its associated value:

    index_by_name = {"Ada": 0, "Grace": 1}
    index_by_name["Ada"]  # 0

Dictionary lookup and insertion are O(1) on average, not a guarantee for every possible input. Hash collisions can occur, and worst-case operations can be slower. Dictionary keys must be hashable; common immutable values such as strings and integers are hashable.

## 3. Two Sum with a dictionary

For each number, calculate the complement needed to reach the target. Check whether that complement has already appeared. If it has, return the earlier index and the current index. Otherwise, store the current number and its index.

    def two_sum(nums, target):
        seen = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], i]
            seen[number] = i

The lookup happens before insertion. This prevents using the same array element twice.

## Worked trace

For nums = [3, 2, 4], target = 6:
- Read 3; complement is 3; it is not in seen. Store {3: 0}.
- Read 2; complement is 4; it is not present. Store {3: 0, 2: 1}.
- Read 4; complement is 2; index 1 is in seen. Return [1, 2].

Expected time: O(n), because each item performs a constant number of average-case dictionary operations. Auxiliary space: O(n), because the dictionary may store up to n values.

## Compare the approaches

| Approach | Time | Auxiliary space |
|---|---:|---:|
| Nested loops | O(n²) | O(1) |
| Dictionary | O(n) expected | O(n) |

The faster approach uses extra memory. This is a common algorithmic trade-off.

## Check your understanding

Explain why the dictionary lookup must happen before storing the current number, especially when the input contains two equal values.

**Practice:** implement the one-pass hash map version and compare it with your brute-force version. The file in solutions/ is starter code.
