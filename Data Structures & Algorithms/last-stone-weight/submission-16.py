import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            res = (-1 * heapq.heappop(stones)) - (-1*heapq.heappop(stones))
            heapq.heappush(stones, -1*res)

        return -1*heapq.heappop(stones)

            

        