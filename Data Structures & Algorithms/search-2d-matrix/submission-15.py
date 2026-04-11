class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1

        for i in range(len(matrix)):
            if target > matrix[i][r]:
                continue
            else:
                while l <= r:
                    m = (l+r) // 2
                    if matrix[i][m] == target:
                        return True
                    if matrix[i][m] < target:
                        l = m+1
                    elif matrix[i][m] > target:
                        r = m-1

        return False