class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = float("-inf")
        l = 0
        window = {}
        maxF = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxF = max(window[s[r]], maxF)

            while r-l+1-maxF > k:
                window[s[l]] = window[s[l]] - 1
                l += 1

            longest = max(longest, r-l+1)
        
        return longest
