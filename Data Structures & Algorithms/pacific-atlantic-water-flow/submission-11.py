class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        pac_deq = deque()
        atl_deq = deque()

        for c in range(cols):
            pac[0][c] = True
            pac_deq.append([0, c])
            atl[rows-1][c] = True
            atl_deq.append([rows-1, c])
        
        for r in range(rows):
            pac[r][0] = True
            pac_deq.append([r, 0])
            atl[r][cols-1] = True
            atl_deq.append([r, cols-1])
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while pac_deq:
            r, c = pac_deq.popleft()            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or pac[nr][nc]):
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    pac[nr][nc] = True
                    pac_deq.append([nr, nc])
        
        while atl_deq:
            r, c = atl_deq.popleft()            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or c < 0 or nr >= rows or nc >= cols or atl[nr][nc]):
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    atl[nr][nc] = True
                    atl_deq.append([nr, nc])
        
        answer = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    answer.append([r, c])
        
        return answer