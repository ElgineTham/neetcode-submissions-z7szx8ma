class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        opt1, opt2 = 0, 0
        rob1, rob2 = 0, 0

        for i in range(len(nums)-1):
            temp = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = temp

        opt1 = rob2
        rob1, rob2 = 0, 0

        for i in range(1, len(nums)):
            temp = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        opt2 = rob2
        return max(opt1,opt2)