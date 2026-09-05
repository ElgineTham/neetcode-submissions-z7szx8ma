class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            last_i = i
            while stack and stack[-1][1] > h:
                last_i, height = stack.pop()
                area = (i - last_i) * height
                max_area = max(max_area, area)
            
            stack.append((last_i, h))
        
        while stack:
            index, height = stack.pop()
            area = (len(heights) - index) * height
            max_area = max(max_area, area)
        
        return max_area