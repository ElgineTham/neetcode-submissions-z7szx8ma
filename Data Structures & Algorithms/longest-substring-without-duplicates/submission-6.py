class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l, r = 0,0
        longest = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            while count[s[r]] > 1 and l < r:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)
            r += 1

        return longest
