class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()

        def mod_grid(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r,c) in seen or grid[r][c] == -1):
                return
            
            q.append([r,c])
            seen.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen.add((r,c))
                    q.append([r,c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                mod_grid(r+1, c)
                mod_grid(r-1, c)
                mod_grid(r, c+1)
                mod_grid(r, c-1)
            dist += 1
