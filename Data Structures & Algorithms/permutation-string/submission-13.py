class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        have, need = {}, {}
        have_total, need_total = 0, 0

        for c in s1:
            if c not in need:
                need[c] = 0
                need_total += 1
            need[c] += 1

            if c not in have:
                have[c] = 0
        
        l = 0
        while l < len(s2):
            if s2[l] in need:
                r = l
                while r < len(s2) and s2[r] in need:
                    have[s2[r]] += 1
                    if have[s2[r]] == need[s2[r]]:
                        have_total += 1
                    while have[s2[r]] > need[s2[r]]:
                        have[s2[l]] -= 1
                        if have[s2[l]] < need[s2[l]]:
                            have_total -= 1
                        l += 1
                    if have_total == need_total:
                        return True
                    r += 1
                while l < r:
                    have[s2[l]] -= 1
                    l += 1
            
            have_total = 0
            l += 1
        
        return False