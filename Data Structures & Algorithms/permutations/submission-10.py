class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        def backtrack(i, combinations):
            if i >= len(nums):
                return [[]]
            
            perms = backtrack(i + 1, combinations)
            new_perms = []
            for p in perms:
                copy = p.copy()
                for idx in range(len(copy) + 1):
                    first_half = copy[:idx]
                    second_half = copy[idx:]
                    combine = first_half + [nums[i]] + second_half
                    new_perms.append(combine)
            
            return new_perms

        return backtrack(0, [])

            