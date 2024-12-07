# Valid Anagram

[Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Sorting


## Hashing

- Time Complexity: O(N)
- Space Complexity: O(N)
- check to see if both strings are equal to each other first. if they are not equal then they cannot be anagrams
- loop through both strings
    - one string adds one to the hashmap[key]
    - other string subtracts one from the hashmap[key]
- if they are anagrams, each key in the hashmap should be equal to 0, false otherwise
