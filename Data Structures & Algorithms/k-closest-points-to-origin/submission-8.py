class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            arr.append([distance, x, y])
        heapq.heapify(arr)

        answer = []
        for i in range(k):
            distance, x, y = heapq.heappop(arr)
            answer.append([x,y])
        return answer