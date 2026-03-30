import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(math.pow(x,2) + math.pow(y,2))
            distances.append([distance, x, y])

        #distances = [[2, 0, 2],[2, 2, 0],[2.4513, 2, 2]]

        heapq.heapify(distances) 
        ans = []   
        for i in range(k):
            curr_point = heapq.heappop(distances)
            ans.append([curr_point[1], curr_point[2]])
        return ans
