class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s))
            ans += ","
        
        ans += "#"

        for s in strs:
            ans += s
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        sizes = []

        i = 0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        
        i += 1

        for size in sizes:
            ans.append(s[i:i+size])
            i += size

        return ans