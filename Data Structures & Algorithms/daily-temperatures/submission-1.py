from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = deque()

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                element = stack.pop()
                day = element[0]
                ans[day] = i - day
            stack.append((i,t))
        
        return ans