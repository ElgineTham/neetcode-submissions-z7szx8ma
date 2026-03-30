from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                else:
                    if element in row[r] or element in col[c] or element in square[(r//3, c//3)]:
                        return False
                    else:
                        row[r].add(element)
                        col[c].add(element)
                        square[(r//3,c//3)].add(element)
        
        return True