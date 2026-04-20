class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_map = collections.defaultdict(list)  # [src : (trg, time)]
        for src, trg, time in times:
            node_map[src].append((trg,time))
        
        heap = [(0,k)]  # (time, target)
        heapq.heapify(heap)
        seen = set()

        t = 0
        while heap:
            time1, node1 = heapq.heappop(heap)
            if node1 in seen:
                continue
            
            seen.add(node1)
            t = time1

            for node2, time2 in node_map[node1]:
                if node2 in seen:
                    continue
                heapq.heappush(heap, (time1 + time2, node2)) 

        if len(seen) != n:
            return -1
        
        return t