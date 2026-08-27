class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxL = heights[0]
        maxR = heights[-1]
        l, r = 0, len(heights)-1
        
        amount = 0

        while l < r:
            if maxL <= maxR:
                amount = max(amount, (r-l)*maxL)
                l += 1
                maxL = max(maxL, heights[l])
            else:
                amount = max(amount, (r-l)*maxR)
                r -= 1
                maxR = max(maxR, heights[r])

        return amount
            

