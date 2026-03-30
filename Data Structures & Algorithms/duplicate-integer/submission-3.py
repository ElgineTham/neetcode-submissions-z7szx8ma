class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for l in range(len(nums)):
            if nums[l] in seen:
                return True
            seen.add(nums[l])
        return False
        