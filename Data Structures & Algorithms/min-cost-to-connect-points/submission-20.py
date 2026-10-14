class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nei = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                
                cost = (abs(points[i][0] - points[j][0]) 
                        + abs(points[i][1] - points[j][1]))
                nei[i].append([cost, j])
        
        heap = [[0, 0]]
        total_cost = 0
        seen = set()

        while len(seen) < len(points):
            cost, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            total_cost += cost

            for nei_cost, j in nei[i]:
                if j in seen:
                    continue
                heapq.heappush(heap, [nei_cost, j])
        
        return total_cost