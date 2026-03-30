class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = set()
        seen = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    rotten.append([r,c])
                if grid[r][c] == 1:
                    fresh.add((r,c))

        def addFruit(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == 0 or (r,c) in seen):
                return
            
            seen.add((r,c))
            rotten.append([r,c])
            if (r,c) in fresh:
                fresh.remove((r,c))
        
        minute = 0
        while rotten:
            minute += 1

            for i in range(len(rotten)):
                r, c = rotten.popleft()
                grid[r][c] = 2
                addFruit(r+1,c)
                addFruit(r-1,c)
                addFruit(r,c+1)
                addFruit(r,c-1)
        
        if fresh:
            return -1
        
        return minute-1 if minute > 0 else minute