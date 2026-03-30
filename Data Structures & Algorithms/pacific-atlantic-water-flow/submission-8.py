class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False] * cols for i in range(rows)]
        atl = [[False] * cols for i in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(source, ocean):
            seen = set()
            q = deque(source)
            while q:
                r,c = q.popleft()
                ocean[r][c] = True
                seen.add((r,c))
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        (nr,nc) not in seen and heights[nr][nc] >=
                        heights[r][c]):
                        q.append((nr,nc))

        pacific = []
        atlantic = []

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols-1))
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows-1, c))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        answer = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    answer.append([r,c])

        return answer