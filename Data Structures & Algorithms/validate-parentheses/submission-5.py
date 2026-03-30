from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for r in range(len(s)):
            if s[r] == '}':
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != '{':
                    return False
            elif s[r] == ']':
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != '[':
                    return False
            elif s[r] == ')':
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != '(':
                    return False
            else:
                stack.append(s[r])
        
        if stack:
            return False
        else:
            return True