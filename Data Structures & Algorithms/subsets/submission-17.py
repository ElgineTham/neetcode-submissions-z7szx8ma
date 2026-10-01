class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        
        answer = []
        def backtrack(idx, arr):
            if idx >= len(nums):
                answer.append(arr.copy())
                return

            arr.append(nums[idx])
            backtrack(idx + 1, arr)
            arr.pop()
            backtrack(idx + 1, arr)
        
        backtrack(0, [])
        return answer