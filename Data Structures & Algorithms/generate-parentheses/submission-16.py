class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        answers = []
        curr_string = []
        def backtrack(o, c):
            if o == n and c == n:
                answers.append("".join(curr_string))
                return

            if o < n:
                curr_string.append("(")
                backtrack(o + 1, c)
                curr_string.pop()
            
            if c < o:
                curr_string.append(")")
                backtrack(o, c + 1)
                curr_string.pop()
        
        backtrack(0, 0)
        return answers
