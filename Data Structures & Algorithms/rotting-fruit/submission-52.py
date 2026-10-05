class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fruits = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c])
                
                if grid[r][c] == 1:
                    fruits += 1
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        time = 0
        
        if not rotten and not fruits:
            return 0 

        while rotten:
            time += 1
            length = len(rotten)
            for _ in range(length):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2
                    fruits -= 1
                    rotten.append([nr, nc])
        
        if fruits:
            return -1
        
        return time - 1


