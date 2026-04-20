class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []

        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                if self.is_pali(i, j, s):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()

        dfs(0)
        return res
                    
        
    def is_pali(self, l, r, s):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        
        return True