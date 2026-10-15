class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for s, d, c in flights:
            if s not in adj:
                adj[s] = []
            adj[s].append([d, c])
        
        heap = []
        heap.append([0, src, -1])  # [cost, src, stops]
        seen = set()
        min_cost = float("inf")

        while heap:
            cost, curr, stops = heapq.heappop(heap)

            if curr == dst:
                return cost

            if stops == k:
                continue
            
            if curr not in adj:
                continue
            
            seen.add((curr, stops))

            for nxt_stop, nxt_cost in adj[curr]:
                if (nxt_stop, stops + 1) in seen:
                    continue
                heapq.heappush(heap, [cost + nxt_cost, nxt_stop, stops + 1])

        if min_cost == float("inf"):
            return -1
        
        return min_cost