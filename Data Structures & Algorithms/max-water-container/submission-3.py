class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        l, r = 0, len(heights)-1
        while l < r:
            currentAmount = min(heights[l], heights[r]) * (r-l)
            maxAmount = max(maxAmount, currentAmount)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
        return maxAmount