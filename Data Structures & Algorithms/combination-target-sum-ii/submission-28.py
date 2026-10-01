class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        answer = []
        curr_total = 0
        curr_arr = []
        def backtrack(i, curr_arr):
            nonlocal curr_total
            if curr_total == target:
                answer.append(curr_arr.copy())
                return
            
            if i >= len(candidates) or curr_total > target:
                return
            
            curr_total += candidates[i]
            curr_arr.append(candidates[i])
            backtrack(i + 1, curr_arr)
            curr_total -= candidates[i]
            curr_arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, curr_arr)
        
        backtrack(0, curr_arr)
        return answer