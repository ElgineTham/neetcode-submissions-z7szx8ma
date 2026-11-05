class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        total_max = nums[0]
        curr_max, curr_min = 1, 1

        for i in range(len(nums)):
            if nums[i] == 0:
                curr_max, curr_min = 1, 1
                total_max = max(total_max, 0)
                continue
            candidates = [nums[i] * curr_max, nums[i] * curr_min, nums[i]]
            curr_max = max(candidates)
            curr_min = min(candidates)
            total_max = max(total_max, curr_max, curr_min)
        
        return total_max
