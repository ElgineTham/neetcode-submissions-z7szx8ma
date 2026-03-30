class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        def isValidChar(c):
            char = ord(c)
            if ((char > 47 and char < 58 ) or
                (char > 64 and char < 91) or
                (char > 96 and char < 123)):
                return True
            else: 
                return False

        while l <= r:
            if not isValidChar(s[l]):
                l += 1
            elif not isValidChar(s[r]):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

        return True