class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        seen = set()

        for src, dst, cost in times:
            adj[src].append([dst, cost])
        
        heap = [[0, k]]
        total_t = 0

        while heap:
            curr_t, curr_node = heapq.heappop(heap)
            if curr_node in seen:
                continue
            total_t = curr_t
            seen.add(curr_node)

            for next_node, next_t in adj[curr_node]:
                if next_node in seen:
                    continue
                heapq.heappush(heap, [curr_t + next_t, next_node])
        
        if len(seen) != n:
            return -1
        
        return total_t