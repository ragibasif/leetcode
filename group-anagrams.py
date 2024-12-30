class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap and sort
        # time: O(n * mlogm)
        # space: O(n * m)
        hashmap = {}
        for i in strs:
            sorted_string = ''.join(sorted(i))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(i)
        res = []
        for k,v in hashmap.items():
            res.append(v)
        return res
