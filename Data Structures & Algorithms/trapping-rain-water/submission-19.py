class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l, r = 0, len(height)-1
        maxL, maxR = 0, 0

        total = 0
        while l <= r:
            if maxL <= maxR:
                if maxL - height[l] > 0:
                    total += maxL - height[l]
                maxL = max(maxL, height[l])
                l += 1
            else:
                if maxR - height[r] > 0:
                    total += maxR - height[r]
                maxR = max(maxR, height[r])
                r -= 1
        
        return total