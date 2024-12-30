class Solution:
    def scoreOfString(self, s: str) -> int:
        # simple implementation problem
        # time: O(n)
        # space: O(1)
        result = 0
        for i in range(1,len(s),1):
            result += abs(ord(s[i-1]) - ord(s[i]))
        return result
