"""Behavioral tests for the Week 1 Python DSA exercises.

Run from the repository root:
    python -m unittest discover -s tests -v

These tests intentionally fail while the learner starter functions still contain
TODO/pass. Implement the exercise first; do not replace the tests with expected
outputs copied from an editorial.
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]


def load_function(relative_path: str, function_name: str) -> Callable[..., Any]:
    """Load one exercise module without requiring package __init__.py files."""
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(
        f"week01_{path.stem}", path
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load exercise module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    function = getattr(module, function_name, None)
    if not callable(function):
        raise TypeError(f"{path} must define callable {function_name}()")
    return function


contains_duplicate = load_function(
    "weeks/week-01/day-01/solutions/contains_duplicate.py",
    "contains_duplicate",
)
is_anagram = load_function(
    "weeks/week-01/day-02/solutions/valid_anagram.py",
    "is_anagram",
)
two_sum_brute = load_function(
    "weeks/week-01/day-03/solutions/two_sum_brute_force.py",
    "two_sum",
)
two_sum_hashmap = load_function(
    "weeks/week-01/day-04/solutions/two_sum_hashmap.py",
    "two_sum",
)
is_palindrome = load_function(
    "weeks/week-01/day-05/solutions/valid_palindrome.py",
    "is_palindrome",
)
group_anagrams = load_function(
    "weeks/week-01/day-06/solutions/group_anagrams.py",
    "group_anagrams",
)


def assert_valid_two_sum(
    testcase: unittest.TestCase,
    function: Callable[[list[int], int], Any],
    nums: list[int],
    target: int,
) -> None:
    result = function(nums, target)
    testcase.assertIsInstance(result, (list, tuple))
    testcase.assertEqual(len(result), 2)
    first, second = result
    testcase.assertIsInstance(first, int)
    testcase.assertIsInstance(second, int)
    testcase.assertNotEqual(first, second, "an element cannot be used twice")
    testcase.assertGreaterEqual(first, 0)
    testcase.assertGreaterEqual(second, 0)
    testcase.assertLess(first, len(nums))
    testcase.assertLess(second, len(nums))
    testcase.assertEqual(nums[first] + nums[second], target)


def normalise_groups(groups: Any) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


class TestContainsDuplicate(unittest.TestCase):
    def test_duplicate_at_different_positions(self) -> None:
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))

    def test_no_duplicate(self) -> None:
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_empty_and_single_item_inputs(self) -> None:
        self.assertFalse(contains_duplicate([]))
        self.assertFalse(contains_duplicate([42]))

    def test_negative_and_zero_values(self) -> None:
        self.assertTrue(contains_duplicate([-1, 0, -1]))


class TestValidAnagram(unittest.TestCase):
    def test_positive_case(self) -> None:
        self.assertTrue(is_anagram("anagram", "nagaram"))

    def test_negative_case(self) -> None:
        self.assertFalse(is_anagram("rat", "car"))

    def test_length_mismatch(self) -> None:
        self.assertFalse(is_anagram("a", "ab"))

    def test_repeated_character_counts_matter(self) -> None:
        self.assertFalse(is_anagram("aab", "abb"))

    def test_empty_strings(self) -> None:
        self.assertTrue(is_anagram("", ""))


class TestTwoSum(unittest.TestCase):
    def test_brute_force_examples(self) -> None:
        assert_valid_two_sum(self, two_sum_brute, [2, 7, 11, 15], 9)
        assert_valid_two_sum(self, two_sum_brute, [3, 2, 4], 6)
        assert_valid_two_sum(self, two_sum_brute, [3, 3], 6)

    def test_hash_map_examples(self) -> None:
        assert_valid_two_sum(self, two_sum_hashmap, [2, 7, 11, 15], 9)
        assert_valid_two_sum(self, two_sum_hashmap, [3, 2, 4], 6)
        assert_valid_two_sum(self, two_sum_hashmap, [3, 3], 6)

    def test_negative_values(self) -> None:
        assert_valid_two_sum(self, two_sum_brute, [-3, 4, 3, 90], 0)
        assert_valid_two_sum(self, two_sum_hashmap, [-3, 4, 3, 90], 0)

    def test_same_element_cannot_be_reused(self) -> None:
        for function in (two_sum_brute, two_sum_hashmap):
            with self.subTest(function=function.__module__):
                assert_valid_two_sum(self, function, [3, 2, 4], 6)


class TestValidPalindrome(unittest.TestCase):
    def test_canonical_palindrome(self) -> None:
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self) -> None:
        self.assertFalse(is_palindrome("race a car"))

    def test_ignores_punctuation_and_case(self) -> None:
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_empty_or_non_alphanumeric_input(self) -> None:
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("   ,.!"))

    def test_single_character(self) -> None:
        self.assertTrue(is_palindrome("Z"))


class TestGroupAnagrams(unittest.TestCase):
    def test_groups_words_by_character_frequency(self) -> None:
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertEqual(normalise_groups(group_anagrams(words)), normalise_groups(expected))

    def test_empty_input(self) -> None:
        self.assertEqual(group_anagrams([]), [])

    def test_empty_string_and_single_character(self) -> None:
        self.assertEqual(
            normalise_groups(group_anagrams([""])),
            [[""]],
        )
        self.assertEqual(
            normalise_groups(group_anagrams(["a"])),
            [["a"]],
        )

    def test_repeated_words_remain_repeated(self) -> None:
        self.assertEqual(
            normalise_groups(group_anagrams(["ab", "ba", "ab"])),
            [["ab", "ab", "ba"]],
        )


if __name__ == "__main__":
    unittest.main()
