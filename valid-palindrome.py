class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # strip non alnum and convert char to lower
        # time: O(n)
        # space: O(1)
        c = ""
        for i in range(0,len(s)):
            if (s[i].isalnum()):
                c += s[i].lower()
        l = 0
        r = len(c)-1
        while l <= r:
            if c[l] != c[r]:
                return False
            l += 1
            r -= 1
        return True
