class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        seen = set()
        perms = self.permuteUnique(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                if tuple(p_copy) not in seen:
                    res.append(p_copy)
                    seen.add(tuple(p_copy))

        return res