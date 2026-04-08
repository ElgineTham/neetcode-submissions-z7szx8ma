class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}

        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in sumMap:
                return [sumMap[target-num], i]
            sumMap[num] = i
        