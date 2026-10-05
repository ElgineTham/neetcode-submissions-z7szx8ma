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
                return 0
            
            seen.add((r, c))
            
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            up = dfs(r-1, c)
            down = dfs(r+1, c)

            return 1 + left + right + up + down
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    curr_area = 0
                    max_area = max(max_area, dfs(r, c))
        
        return max_area

