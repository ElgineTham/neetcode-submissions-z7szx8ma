class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            last = len(row)-1
            if row[last] >= target:
                first = 0
                while first <= last:
                    middle = (first+last)//2
                    if row[middle] == target:
                        return True

                    if row[middle] > target:
                        last = middle-1
                    else:
                        first = middle+1
        
        return False