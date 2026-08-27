class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        maxL, maxR = height[0], height[-1]
        amount = 0
        l, r = 1, len(height)-2

        while l <= r:
            if maxL <= maxR:
                if maxL > height[l]:
                    amount += maxL - height[l]
                maxL = max(maxL, height[l])
                l += 1
            else:
                if maxR > height[r]:
                    amount += maxR - height[r]
                maxR = max(maxR, height[r])
                r -= 1
        
        return amount