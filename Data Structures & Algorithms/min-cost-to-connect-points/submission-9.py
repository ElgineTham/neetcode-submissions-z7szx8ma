class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        seen = set()
        heap = [[0,0]]
        while len(seen) < len(points):
            cost, i = heapq.heappop(heap)
            if i in seen:
                continue
            res += cost
            seen.add(i)
            for j in range(len(points)):
                if j == i or j in seen:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, [dist, j])
        
        return res
