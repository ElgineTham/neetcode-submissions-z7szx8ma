class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        a, b = s1, s2
        
        count_a = {}
        for s in a:
            count_a[s] = count_a.get(s, 0) + 1
        total_a = sum(count_a.values())
        
        for l in range(len(b)):
            have = False
            if b[l] in count_a:
                count_b = {}
                r = l
                while r - l < len(a) and r < len(b):
                    if b[r] not in count_a:
                        break
                    count_b[b[r]] = count_b.get(b[r], 0) + 1
                    if count_b[b[r]] > count_a[b[r]]:
                        break
                    r += 1
            
                if (len(count_b.keys()) == len(count_a.keys())
                    and sum(count_b.values()) == 
                    sum(count_a.values())):
                    have = True
            
            if have:
                return True

        return False         

