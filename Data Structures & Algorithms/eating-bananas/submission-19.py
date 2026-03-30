import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        first, last = 1, max(piles)
        minT = float("inf")
        minR = float("inf")

        while first <= last:
            rate = (first+last)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            if time > h:
                first = rate+1
            elif time <= h:
                minT = time
                minR = rate
                last = rate-1

        return minR

            