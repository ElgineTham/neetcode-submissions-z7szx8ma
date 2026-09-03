class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        have, need = 0, 0
        countT, countS = {}, {}
        shortestLength, shortestIndex = float("inf"), [-1, -1]

        for char in t:
            if char not in countT:
                countS[char] = 0
                need += 1
            countT[char] = countT.get(char, 0) + 1

        left = 0
        for right in range(len(s)):
            if s[right] in countT:
                countS[s[right]] = countS.get(s[right], 0) + 1
                if countS[s[right]] == countT[s[right]]:
                    have += 1

            while have == need:
                if shortestLength > right - left + 1:
                    shortestLength = right-left+1
                    shortestIndex[0] = left
                    shortestIndex[1] = right
                if s[left] in countT:
                    countS[s[left]] = countS.get(s[left]) - 1
                    if countS.get(s[left]) < countT.get(s[left]):
                        have -= 1
                left += 1

        return s[shortestIndex[0]:shortestIndex[1]+1]
