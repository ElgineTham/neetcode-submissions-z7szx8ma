class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]

        strs.sort()

        ans = ""
        first = strs[0]
        last = strs[-1]

        for i in range(len(first)):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break

        return ans

