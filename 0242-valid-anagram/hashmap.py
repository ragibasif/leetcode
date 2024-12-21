class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
        # time: O(N)
        # space: O(N)
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        for j in t:
            if j not in hashmap:
                hashmap[j] = 0
            hashmap[j] -= 1
        for k,v in hashmap.items():
            if v != 0:
                return False
        return True
