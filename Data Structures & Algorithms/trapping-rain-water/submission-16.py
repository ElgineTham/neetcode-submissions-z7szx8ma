class Solution:
    def trap(self, height: List[int]) -> int:
        left_bound, right_bound = 0, 0
        l, r = 0, len(height)-1
        total = 0

        while l <= r:
            if left_bound <= right_bound:
                h = min(left_bound, right_bound) - height[l] 
                if h > 0:
                    total += h
                left_bound = max(left_bound, height[l])
                l += 1
            else:
                h = min(left_bound, right_bound) - height[r]
                if h > 0:
                    total += h
                right_bound = max(right_bound, height[r])
                r -= 1
        
        return total
