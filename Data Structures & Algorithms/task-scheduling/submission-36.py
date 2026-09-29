class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1
        
        heap = [(-freq, task) for task, freq in freq_map.items()]
        heapq.heapify(heap)
        cycles = 0
        cooldown = deque()

        while heap or cooldown:
            cycles += 1
            curr_task = heapq.heappop(heap) if heap else None

            if curr_task:
                if curr_task[0] + 1 < 0:
                    cooldown.append((cycles + n, (curr_task[0] + 1, curr_task[1])))
            
            if cooldown:
                if cooldown[0][0] == cycles:
                    popped = cooldown.popleft()
                    heapq.heappush(heap, popped[1])
        
        return cycles