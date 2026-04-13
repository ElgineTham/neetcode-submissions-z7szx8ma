class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = defaultdict(int)
        for task in tasks:
            taskMap[task] += 1

        heap = []
        for task in taskMap:
            heap.append(-taskMap[task])
        heapq.heapify(heap)
        
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1

            if heap:
                curr_task = heapq.heappop(heap) + 1
                if curr_task:
                    cooldown.append((curr_task, time+n))
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
        
        return time


