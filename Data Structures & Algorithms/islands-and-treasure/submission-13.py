class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        treasure = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    treasure.append([r, c])
        
        if not treasure:
            return
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while treasure:
            r, c = treasure.popleft()
            for dr, dc in directions:
                r1, c1 = r + dr, c + dc
                if (r1 < 0 or c1 < 0 or r1 >= rows or c1 >= cols
                    or grid[r1][c1] != 2147483647):
                    continue
                
                grid[r1][c1] = grid[r][c] + 1
                treasure.append([r1, c1])
        

        


