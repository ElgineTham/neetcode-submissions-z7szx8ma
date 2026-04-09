class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        result = 0
        sellP, buyP = prices[0], prices[0]
        for price in prices:
            if price < buyP:
                result = max(result, sellP - buyP)
                sellP, buyP = price, price
            if price > sellP:
                sellP = price
        
        return max(result, sellP-buyP)

