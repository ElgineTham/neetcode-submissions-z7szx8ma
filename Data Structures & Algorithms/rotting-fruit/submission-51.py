class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        fresh = set()
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                if grid[r][c] == 2:
                    rotten.append((r,c))
        
        time = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while rotten:
            if len(fresh) == 0:
                return time
            
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                if ((r,c)) in seen:
                    continue
                seen.add((r,c))

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols
                        or grid[nr][nc] == 0 or (nr,nc) in seen):
                        continue
                    
                    if (nr,nc) in fresh:
                        fresh.remove((nr,nc))
                    
                    rotten.append((nr,nc))
            
            time += 1
        
        if len(fresh) > 0:
            return -1
        
        return time