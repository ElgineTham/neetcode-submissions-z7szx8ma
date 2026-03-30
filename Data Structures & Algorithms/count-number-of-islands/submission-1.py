class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r,c) in seen or grid[r][c] == "0"):
                return False
            
            if grid[r][c] == "1":
                seen.add((r,c))
            
            res = (dfs(r+1,c),
                    dfs(r-1,c),
                    dfs(r,c+1),
                    dfs(r,c-1))
            
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    islands += 1
                    dfs(r, c)
        
        return islands