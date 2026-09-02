class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        longest = 0
        l, r = 0, 0

        seen = set()
        
        while r < len(s):            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            longest = max(longest, r-l+1)
            r += 1
        
        return longest