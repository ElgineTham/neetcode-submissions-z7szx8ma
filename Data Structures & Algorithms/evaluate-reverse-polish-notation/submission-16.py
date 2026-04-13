class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                if token == '/':
                    num2 = stack.pop()
                    num1 = stack.pop()

                    result = int(num1 / num2)
                    stack.append(result)
                elif token == '+':
                    num2 = stack.pop()
                    num1 = stack.pop()

                    result = num1 + num2
                    stack.append(result)
                elif token == '-':
                    num2 = stack.pop()
                    num1 = stack.pop()

                    result = num1 - num2
                    stack.append(result)
                elif token == '*':
                    num2 = stack.pop()
                    num1 = stack.pop()

                    result = num1 * num2
                    stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
