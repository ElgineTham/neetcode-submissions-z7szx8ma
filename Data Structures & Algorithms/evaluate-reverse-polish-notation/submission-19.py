class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0

        for c in tokens:
            if c == '+':
                c1 = stack.pop()
                c2 = stack.pop()
                stack.append(c1 + c2)
            elif c == '-':
                c1 = stack.pop()
                c2 = stack.pop()
                stack.append(c2 - c1)
            elif c == '*':
                c1 = stack.pop()
                c2 = stack.pop()
                stack.append(c2 * c1)
            elif c == '/':
                c1 = stack.pop()
                c2 = stack.pop()
                stack.append(int(c2 / c1))
            else:
                stack.append(int(c))
        
        return stack.pop()