class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [num for num in nums]
        heapq.heapify(self.heap)
        self.max_length = k
        while len(self.heap) > self.max_length:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.max_length:
            heapq.heappop(self.heap)

        return self.heap[0]

