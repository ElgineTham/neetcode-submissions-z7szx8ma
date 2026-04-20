class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        curr = []
        def backtrack(i, total):
            if total == target:
                ans.append(curr.copy())
                return 

            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i+1, total+candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            backtrack(i+1, total)
        
        backtrack(0, 0)

        return ans