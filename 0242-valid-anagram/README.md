# Valid Anagram

[Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Sorting

<!--TODO-->

## Hashing

- Time Complexity: O(N)
- Space Complexity: O(N)
- check to see if both strings are equal to each other first. if they are not equal then they cannot be anagrams
- loop through both strings
    - one string adds one to the hashmap[key]
    - other string subtracts one from the hashmap[key]
- if they are anagrams, each key in the hashmap should be equal to 0, false otherwise

```C++
// C++ hash hable holution
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> hashmap;
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            if (hashmap.find(s[i]) != hashmap.end()) { // it exists
                hashmap[s[i]]++;
            } else {
                hashmap[s[i]] = 1;
            }
            if (hashmap.find(t[i]) != hashmap.end()) { // it exists
                hashmap[t[i]]--;
            } else {
                hashmap[t[i]] = -1;
            }
        }
        // using iterators to check each item
        for (auto it = hashmap.begin(); it != hashmap.end(); it++) {
            if (it->second != 0) {
                return false;
            }
        }
        return true;
    }
};
```
