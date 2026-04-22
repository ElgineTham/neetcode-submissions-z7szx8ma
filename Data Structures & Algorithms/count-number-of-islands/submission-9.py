class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                or (r,c) in seen or grid[r][c] == "0"):
                return
            
            seen.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr,nc)
            
            return
        
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    num_islands += 1
                    dfs(r,c)
        
        return num_islands
