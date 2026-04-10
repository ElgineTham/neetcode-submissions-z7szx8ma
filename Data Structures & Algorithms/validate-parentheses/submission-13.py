class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        
        for c in s:
            if c == ')':
                if not q or q.pop() != '(':
                    return False
            elif c == ']':
                if not q or q.pop() != '[':
                    return False
            elif c == '}':
                if not q or q.pop() != '{':
                    return False
            else:
                q.append(c)
        
        return True if not q else False
