class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            distance = math.sqrt((point[0]-0)**2 + (point[1])**2)
            heapq.heappush(closest, (distance, point))
        
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(closest)[1])

        return answer