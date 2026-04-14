class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prefix = [0] * len(nums)
        prefix[0] += nums[0]
        max_total = prefix[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            j = 0
            while j < i:
                max_total = max(prefix[i]-prefix[j], max_total)
                j += 1
            
            max_total = max(max_total, prefix[j])

        return max_total