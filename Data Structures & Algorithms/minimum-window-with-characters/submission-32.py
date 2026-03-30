class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        have, need = 0, 0
        shortest = [-1000, 1000]
        answer = ""

        for char in t:
            if char not in countT:
                need += 1
            countT[char] = countT.get(char, 0) + 1
            window[char] = 0
        
        l, r = 0, 0
        while r < len(s):
            curr_char = s[r]
            if curr_char not in countT:
                r += 1
            else:
                window[curr_char] = window[curr_char] + 1
                if window[curr_char] == countT[curr_char]:
                    have += 1
                while have == need:
                    if r-l+1 < shortest[1]-shortest[0]+1:
                        shortest = [l, r]
                        answer = s[l:r+1]
                    if s[l] in countT:
                        window[s[l]] = window[s[l]] - 1
                        if window[s[l]] < countT[s[l]]:
                            have -= 1
                    l += 1 
                r += 1

        return answer



