class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        curr_total = 0
        def backtrack(i, curr_arr):
            nonlocal curr_total
            if curr_total == target:
                answer.append(curr_arr.copy())
                return
            
            if curr_total > target or i >= len(nums):
                return
            
            curr_arr.append(nums[i])
            curr_total += nums[i]
            backtrack(i, curr_arr)
            curr_arr.pop()
            curr_total -= nums[i]
            backtrack(i + 1, curr_arr)
        
        backtrack(0, [])
        
        return answer