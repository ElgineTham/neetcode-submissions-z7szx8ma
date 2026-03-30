from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hashMap = {")" : "(", "}" : "{", "]" : "["}
        for r in range(len(s)):
            if s[r] in hashMap:
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != hashMap[s[r]]:
                    return False
            else:
                stack.append(s[r])
        
        if stack:
            return False
        else:
            return True