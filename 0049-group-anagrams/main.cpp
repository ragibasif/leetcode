// #include <algorithm>
// https://stackoverflow.com/questions/9107516/sorting-characters-of-a-c-string
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hashmap;
        for (int i = 0; i < strs.size(); i++) {
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            hashmap[temp].push_back(strs[i]);
        }
        vector<vector<string>> result;
        for (auto& it: hashmap) {
            result.push_back(it.second);
        }
        return result;
    }
};
