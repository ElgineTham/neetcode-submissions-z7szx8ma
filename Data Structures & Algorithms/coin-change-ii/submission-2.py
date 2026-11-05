class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        for i in range(len(coins) - 1, -1, -1):
            coin = coins[i]
            for j in range(amount + 1):
                if j == 0:
                    dp[j] = 1
                    continue
                
                right = dp[j - coin] if j - coin >= 0 else 0
                bottom = dp[j]

                dp[j] = right + bottom
        
        return dp[amount]
    
