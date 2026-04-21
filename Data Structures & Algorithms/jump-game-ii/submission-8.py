class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l, r = 0, 0

        jumps = 0
        while r < len(nums):
            jumps += 1
            jump = 0

            for i in range(l, r+1):
                jump = max(jump, nums[i])
            
            l = r + 1
            r += jump

            if r >= len(nums)-1:
                break
            
        return jumps