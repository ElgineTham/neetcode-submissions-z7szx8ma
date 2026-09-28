class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if nums:
            self.q = nums
        else:
            self.q = []
        self.max_length = k
        heapq.heapify(self.q)
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        while len(self.q) > self.max_length:
            heapq.heappop(self.q)
        return self.q[0]

        
