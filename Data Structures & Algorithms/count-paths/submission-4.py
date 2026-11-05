class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        rows, cols = m, n

        def is_valid(r, c):
            return r >= 0 and c >= 0 and r < rows and c < cols

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    grid[r][c] = 1
                    continue

                left = grid[r][c-1] if is_valid(r, c-1) else 0
                top = grid[r-1][c] if is_valid(r-1, c) else 0
                grid[r][c] = left + top
        
        return grid[rows-1][cols-1]

