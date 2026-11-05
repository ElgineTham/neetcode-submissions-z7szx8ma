class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 4:
            return max(nums)
        
        dp1 = [nums[0], max(nums[0], nums[1])]
        for n in range(2, len(nums)-1):
            temp = max(dp1[1], dp1[0] + nums[n])
            dp1[0] = dp1[1]
            dp1[1] = temp
        
        dp2 = [nums[1], max(nums[1], nums[2])]
        for n in range(3, len(nums)):
            temp = max(dp2[1], dp2[0] + nums[n])
            dp2[0] = dp2[1]
            dp2[1] = temp
        
        return max(max(dp1), max(dp2))