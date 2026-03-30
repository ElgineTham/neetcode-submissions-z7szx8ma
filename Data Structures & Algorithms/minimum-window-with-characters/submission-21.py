class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        res, resLength = [-1, -1], float("inf")
        window, countT = {}, {}
        have, need = 0, 0

        for char in t:
            if char not in countT: need += 1
            countT[char] = 1 + countT.get(char, 0)
            window[char] = 0
        
        while r < len(s):
            if s[r] in countT:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window.get(s[r]) == countT.get(s[r]):
                    have += 1
            while have >= need:
                if resLength > r-l+1:
                    res = [l, r]
                    resLength = r-l+1
                if s[l] in countT:
                    window[s[l]] = window[s[l]] - 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
            r += 1
        if resLength != float("-inf"):
            return s[res[0]:res[1]+1]
        else:
            return ""

        