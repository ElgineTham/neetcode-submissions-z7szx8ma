class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, 0
        count_t, count_s = {}, {}
        for letter in t:
            if letter not in count_t:
                count_t[letter] = 0
                count_s[letter] = 0
                need += 1
            count_t[letter] = count_t[letter] + 1
        
        l, r = 0, 0
        shortest = ""
        shortest_length = float("inf")
        short_l, short_r = 0, 0
        while r < len(s):
            if s[r] in count_t:
                count_s[s[r]] = count_s.get(s[r], 0) + 1
            
                if count_s[s[r]] == count_t[s[r]]:
                    have += 1
                
                while have == need:
                    if shortest_length > r-l+1:
                        shortest_length = r-l+1
                        short_l, short_r = l, r
                    
                    if s[l] in count_s:
                        count_s[s[l]] = count_s[s[l]] - 1
                        if count_s[s[l]] < count_t[s[l]]:
                            have -= 1

                    l += 1
            
            r += 1
        
        if shortest_length < float("inf"):
            shortest = s[short_l:short_r + 1]
        return shortest