/*
 * C++ Hash table solution
 * */
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
