class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [1, 2]
        for i in range(n-2):
            one = dp[0]
            two = dp[1]

            dp[0] = two
            dp[1] = one + two
        
        return dp[-1]