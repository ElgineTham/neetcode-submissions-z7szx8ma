class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten, fresh, seen = deque(), set(), set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    rotten.append((r,c))

        time = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while rotten and fresh:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                seen.add((r,c))

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) in fresh:
                        fresh.remove((nr,nc))
                        rotten.append((nr,nc))
                
            time += 1

        return time if not fresh else -1