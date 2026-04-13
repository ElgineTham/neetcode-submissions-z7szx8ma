class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        maxSum = float("-inf")

        for i in range(len(nums)):
            prefix[i] += nums[i]
            if i-1 >= 0:
                prefix[i] += prefix[i-1]

            for j in range(i):
                if prefix[i] - prefix[j] > maxSum:
                    maxSum = prefix[i] - prefix[j]
            
            if prefix[i] > maxSum:
                maxSum = prefix[i]

        return maxSum 