class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        max_area, curr_area = 0, 0

        def dfs(r, c):
            nonlocal curr_area
            nonlocal max_area
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or grid[r][c] == 0 or (r, c) in seen):
                return
            
            seen.add((r, c))

            curr_area += 1
            
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            up = dfs(r-1, c)
            down = dfs(r+1, c)
        
        for r in range(rows):
            for c in range(cols):
                curr_area = 0
                dfs(r, c)
                max_area = max(max_area, curr_area)
        
        return max_area

