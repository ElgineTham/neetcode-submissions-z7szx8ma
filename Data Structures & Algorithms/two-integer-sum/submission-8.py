class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            if (target - val) in seen:
                return [seen[target - val], i]
            
            seen[val] = i