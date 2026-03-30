from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                if (char in rows[r] or
                    char in columns[c] or
                    char in squares[(r//3, c//3)]):
                    return False
                rows[r].add(char)
                columns[c].add(char)
                squares[(r//3, c//3)].add(char)
        
        return True