class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1
        
        heap = []
        for k, v in freq_map.items():
            heap.append(-v)
        
        heapq.heapify(heap)
        q = deque()

        time = 0
        while heap or q:
            time += 1
            if heap:
                task = -heapq.heappop(heap)
                task -= 1
                if task > 0:
                    q.append((task, time+n))
            if q and q[0][1] == time:
                task, time = q.popleft()
                heapq.heappush(heap, -task)
        
        return time