class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        step_1 = 1
        step_2 = 1

        for i in range(n-1, -1, -1):
            if i+1 >= n or i+2 >= n:
                continue
            
            temp = step_1
            step_1 = step_1 + step_2
            step_2 = temp
        
        return step_1 + step_2