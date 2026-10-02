class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()
        
        def dfs(r, c, idx):
            if idx >= len(word):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[idx] or (r, c) in seen):
                return False
            
            seen.add((r, c))
            
            res = (dfs(r+1, c, idx+1) or
                    dfs(r-1, c, idx+1) or
                    dfs(r, c+1, idx+1) or
                    dfs(r, c-1, idx+1))
            
            seen.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                found = dfs(r, c, 0)
                if found:
                    return True
        
        return False
