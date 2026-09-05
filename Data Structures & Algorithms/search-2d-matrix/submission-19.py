class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if m[-1] < target:
                continue
            
            l, r = 0, len(m) - 1
            while l <=r :
                mid = (l+r)//2
                if m[mid] == target:
                    return True
                elif m[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
            return False
            
        return False