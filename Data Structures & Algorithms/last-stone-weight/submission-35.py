class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            remaining = (-heapq.heappop(stones)) - (-heapq.heappop(stones))
            heapq.heappush(stones, -remaining)
        
        return -stones[0]