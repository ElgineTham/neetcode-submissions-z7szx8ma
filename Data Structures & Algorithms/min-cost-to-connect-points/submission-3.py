class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        point_map = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                point_map[i].append([dist, j])
                point_map[j].append([dist, i])
        
        res = 0
        seen = set()
        heap = [[0,0]]
        while len(seen) < len(points):
            cost, i = heapq.heappop(heap)
            if i in seen:
                continue
            res += cost
            seen.add(i)
            for nei_cost, nei in point_map[i]:
                if nei in seen:
                    continue
                heapq.heappush(heap, [nei_cost, nei])
        
        return res
