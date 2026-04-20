class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minDist = [float('inf')] * n
        visited = [False] * n
        minDist[0] = 0

        res = 0

        for _ in range(n):
            i = -1
            for j in range(n):
                if not visited[j] and (i == -1 or minDist[j] < minDist[i]):
                    i = j

            visited[i] = True
            res += minDist[i]

            for j in range(n):
                if not visited[j]:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    minDist[j] = min(minDist[j], dist)

        return res