class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, quad = defaultdict(set), defaultdict(set), defaultdict(set)

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                element = board[r][c]
                if element == '.':
                    continue
                if (element in row[r] or 
                    element in col[c] or 
                    element in quad[(r//3,c//3)]):
                    return False
                
                row[r].add(element)
                col[c].add(element)
                quad[(r//3,c//3)].add(element)

        return True