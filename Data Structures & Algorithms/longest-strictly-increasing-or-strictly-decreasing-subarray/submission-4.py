class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        longest = 0
        l = 0
        increasing = True
        for r in range(1, len(nums)):
            if nums[r-1] == nums[r]:
                l = r
                longest = max(longest, 1)
                continue

            if increasing:
                if nums[r-1] < nums[r]:
                    longest = max(longest, r-l+1)
                else:
                    increasing = False
                    l = r-1
            else:
                if nums[r-1] > nums[r]:
                    longest = max(longest, r-l+1)
                else:
                    increasing = True
                    l = r-1
        
        return longest
