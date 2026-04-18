class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        count, min_length = 0, float("inf")

        while r < len(nums):
            count += nums[r]

            while count >= target and l <= r:
                min_length = min(min_length, r-l+1)
                count -= nums[l]
                l += 1
            
            r += 1
        
        if min_length == float("inf"):
            return 0
        return min_length