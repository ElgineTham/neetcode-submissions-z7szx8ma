class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]

        nums.sort()

        answer = []
        curr_arr = []
        def backtrack(i):
            if i >= len(nums):
                answer.append(curr_arr.copy())
                return
            
            curr_arr.append(nums[i])
            backtrack(i + 1)
            curr_arr.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return answer