class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        node_map = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                if j == i:
                    continue
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                node_map[i].append([dist, j])
        
        res = 0
        heap = [[0,0]]
        seen = set()
        while len(seen) < len(points):
            cost, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            res += cost

            for nei_cost, nei in node_map[i]:
                if nei in seen:
                    continue
                heapq.heappush(heap, [nei_cost, nei])
        
        return res