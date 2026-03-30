class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        
        subsets = []
        def dfs(i):
            if i >= len(nums):
                return
            
            subsets.append(nums[i])
            res.append(subsets.copy())
            dfs(i + 1)

            subsets.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res