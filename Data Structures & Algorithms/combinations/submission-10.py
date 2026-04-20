class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        curr = []
        def backtrack(i):
            if i > n:
                if len(curr) == k:
                    ans.append(curr.copy())
                return

            curr.append(i)
            backtrack(i+1)
            curr.pop()
            backtrack(i+1)
        
        backtrack(1)

        return ans