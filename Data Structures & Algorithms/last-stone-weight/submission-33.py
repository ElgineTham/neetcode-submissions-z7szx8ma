class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = -heapq.heappop(stones), -heapq.heappop(stones)
            remaining = first - second

            if remaining > 0:
                heapq.heappush(stones, -remaining)
        
        return -stones[0] if stones else 0