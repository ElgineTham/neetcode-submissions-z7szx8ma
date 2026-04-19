class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = len(board), len(board[0])
        rows, cols, square = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(row):
            for c in range(col):
                element = board[r][c]
                if element == '.':
                    continue
                if element in rows[r] or element in cols[c] or element in square[(r//3, c//3)]:
                    return False
                
                rows[r].add(element)
                cols[c].add(element)
                square[(r//3,c//3)].add(element)

        return True
                