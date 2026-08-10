class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, reg = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                element = board[r][c]
                
                if element == ".":
                    continue

                if (element in rows[r] 
                    or element in cols[c] 
                    or element in reg[(r//3, c//3)]):
                    return False
                
                rows[r].add(element)
                cols[c].add(element)
                reg[(r//3, c//3)].add(element)
        
        return True
