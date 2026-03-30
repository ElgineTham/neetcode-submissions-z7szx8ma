class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        seen = set()

        for r in range(rows):
            if board[r][0] == "O":
                board[r][0] = "T"
            if board[r][cols-1] == "O":
                board[r][cols-1] = "T"
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "T"
            if board[rows-1][c] == "O":
                board[rows-1][c] = "T"

        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r,c) in seen or board[r][c] == "X"):
                return

            seen.add((r,c))
            if board[r][c] == "O":
                board[r][c] = "T"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"