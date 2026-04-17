class Solution:
    def reverseBits(self, n: int) -> int:
        bit = bin(n)[2:].zfill(32)
        bit = list(bit)
        l, r = 0, len(bit)-1
        while l < r:
            bit[l], bit[r] = bit[r], bit[l]
            l += 1
            r -= 1
        return int("".join(bit), 2)