class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        output = 0
        maxL, maxR = height[0],height[len(height)-1]
        l, r = 1, len(height)-2
        while l <= r:
            if maxL <= maxR:
                store = min(maxL, maxR) - height[l]
                if store > 0:
                    output += store
                maxL = max(maxL, height[l])
                l += 1
            else:
                store = min(maxL, maxR) - height[r]
                if store > 0:
                    output += store
                maxR = max(maxR, height[r])
                r -= 1

        return output
