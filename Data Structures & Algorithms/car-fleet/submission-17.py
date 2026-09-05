class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted([(p, s) for p, s in zip(position, speed)])
        for p, s in cars:
            curr = (target - p) / s
            while stack and curr >= stack[-1]:
                stack.pop()
            
            stack.append(curr)

        return len(stack)