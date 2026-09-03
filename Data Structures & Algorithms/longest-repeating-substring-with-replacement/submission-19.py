class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return len(s)

        if len(s) == 1:
            return 1
        
        window = {}
        l, r = 0, 0
        most = 0
        longest = 0

        while r < len(s):
            if s[r] not in window:
                window[s[r]] = 0
            
            window[s[r]] += 1
            most = max(most, window[s[r]])

            while r - l + 1 - most > k:
                window[s[l]] = window[s[l]] - 1
                if window[s[l]] == 0:
                    window.pop(s[l])
                most = 0
                for letter, freq in window.items():
                    most = max(most, freq)
                l += 1
            
            longest = max(longest, r-l+1)
            r += 1
    
        return longest
            
            
