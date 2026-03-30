class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        q = deque()

        time = 0
        while heap or q:
            time += 1
            
            if heap:
                task = heapq.heappop(heap) + 1
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time
