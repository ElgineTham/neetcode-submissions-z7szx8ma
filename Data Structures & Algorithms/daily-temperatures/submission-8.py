class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                popped_ind, popped_temp = stack.pop()
                answer[popped_ind] = i - popped_ind
            
            stack.append((i, temp))
        
        return answer
