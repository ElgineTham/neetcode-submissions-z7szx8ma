class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = [0, 0], 0

        for i in range(len(s)):
            # odd
            l,r = i,i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = [l, r]
                l -= 1
                r += 1
            
            # even
            l, r = i, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = [l,r]
                l -= 1
                r += 1

        return s[res[0]:res[1]+1]