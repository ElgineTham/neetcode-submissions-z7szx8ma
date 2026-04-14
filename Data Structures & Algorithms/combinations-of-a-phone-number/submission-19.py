class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dig_to_let = {}
        dig_to_let[2] = ['a','b','c']
        dig_to_let[3] = ['d','e','f']
        dig_to_let[4] = ['g','h','i']
        dig_to_let[5] = ['j','k','l']
        dig_to_let[6] = ['m','n','o']
        dig_to_let[7] = ['p','q','r','s']
        dig_to_let[8] = ['t','u','v']
        dig_to_let[9] = ['w','x','y','z']

        answer = []
        phone = []
        def dfs(i):
            if i >= len(digits):
                answer.append("".join(phone))
                return
            
            for letter in dig_to_let[int(digits[i])]:
                phone.append(letter)
                dfs(i+1)
                phone.pop()
        
        dfs(0)

        return answer