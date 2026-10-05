class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        bdr_circ = deque()
        perm = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            if board[r][0] == "O":
                bdr_circ.append([r, 0])
                perm[r][0] = True
            
            if board[r][cols-1] == "O":
                bdr_circ.append([r, cols-1])
                perm[r][cols-1] = True
        
        for c in range(cols):
            if board[0][c] == "O":
                bdr_circ.append([0, c])
                perm[0][c] = True
            
            if board[rows-1][c] == "O":
                bdr_circ.append([rows-1, c])
                perm[rows-1][c] = True
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while bdr_circ:
            r, c = bdr_circ.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or board[nr][nc] == "X"
                    or perm[nr][nc]):
                    continue
                
                perm[nr][nc] = True
                bdr_circ.append([nr, nc])
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not perm[r][c]:
                    board[r][c] = "X"
        