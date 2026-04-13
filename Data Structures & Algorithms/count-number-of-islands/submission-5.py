class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen, rows, cols = set(), len(grid), len(grid[0])
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r,c) in seen or grid[r][c] == "0"):
                return False
            
            if grid[r][c] == "1":
                seen.add((r,c))
            down = dfs(r+1, c)
            up = dfs(r-1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)

            return down or up or left or right
        
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    num_islands += 1
                    dfs(r, c)

        return num_islands
