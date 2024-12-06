# Contains Duplicate

[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

<!--TODO-->

## Brute force

- 2 nested for loops
- Time Complexity: O(N^2)
- Space Complexity: O(1)

<!--TODO-->

## Sorting

## Hashing

- loop through each element in the input and check whether its already in the hash table, if it is then return true, if not then add it to the hash table
- Time Complexity: O(N)
- Space Complexity: O(N)

```C++
// C++ Hash table solution
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> hashmap;
        for (int i = 0; i < nums.size(); i++) {
            if (hashmap[nums[i]]) {
                return true;
            }
            hashmap[nums[i]] = true;
        }
        return false;
    }
};
```
