class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, num):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == "0" or (r, c) in seen):
                return
            
            seen.add((r, c))

            left = dfs(r, c-1, num)
            right = dfs(r, c+1, num)
            up = dfs(r-1, c, num)
            down = dfs(r+1, c, num)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    dfs(r, c, 0)
        
        return count
