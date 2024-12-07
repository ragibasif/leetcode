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
