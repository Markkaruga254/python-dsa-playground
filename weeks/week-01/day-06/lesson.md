# Day 06 — Strings, dictionaries, and Group Anagrams

## Learning goals

Use string slicing and dictionary methods, understand hashable keys, and group words by a shared anagram signature.

## 1. Strings

Python strings are immutable sequences of Unicode code points. You can index and slice them, but you cannot change one character in place.

    word = "hello"
    word[1:4]  # "ell"

Methods such as lower(), strip(), and split() return new values rather than mutating the original string.

## 2. Dictionary operations and hashable keys

A dictionary maps hashable keys to values. Lists are mutable and unhashable, so they cannot be dictionary keys. Tuples are hashable only when every element inside the tuple is itself hashable.

dict.get(key, default) returns the value for a key, or the supplied default when the key is absent:

    counts = {"a": 2}
    counts.get("z", 0)  # 0

## 3. Group Anagrams

Words are anagrams when their character frequencies match. To group them, create a signature that is identical for every anagram.

**Sorted-string signature**

    key = "".join(sorted(word))

Words such as "eat", "tea", and "ate" all produce "aet". Use that signature as a dictionary key and append each word to the corresponding group.

If there are n words of maximum length k, sorting each word costs O(k log k), giving O(n · k log k) time overall (ignoring output construction). The grouping dictionary and stored words require O(n · k) space for the output and groups; the auxiliary dictionary keys also consume space.

**Frequency-count signature**

For a known alphabet of 26 lowercase English letters, count each letter and use the 26-count tuple as a key. Building each signature takes O(k), so the total expected time is O(n · k), with O(n) group entries plus output storage. This assumes the input constraint is lowercase English letters; for arbitrary Unicode text, adapt the representation.

## Worked trace

For ["eat", "tea", "tan"]:
- "eat" maps to "aet"; create that group.
- "tea" also maps to "aet"; append it to the same group.
- "tan" maps to "ant"; create a second group.

The final group order is not important unless the problem explicitly requires it.

## Check your understanding

Explain why the signature must be hashable, why a list of sorted characters cannot be used directly as a dictionary key, and how the input constraints affect the complexity of the frequency-count method.

**Practice:** implement the sorted-string signature first. The file in solutions/ is starter code.
