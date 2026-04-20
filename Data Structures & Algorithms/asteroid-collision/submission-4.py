class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            # diff directions
            while (len(stack) >= 2 and 
                    (stack[-2] > 0 and stack[-1] < 0)) :
                s1 = stack.pop()
                s2 = stack.pop()
                if abs(s1) > abs(s2):
                    stack.append(s1)
                elif abs(s1) < abs(s2):
                    stack.append(s2) 
        
        return stack