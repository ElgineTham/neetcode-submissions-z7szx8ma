class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, t = stack.pop()
                answer[i] = ind - i
            
            stack.append((ind, temp))

        return answer
