class MedianFinder:

    def __init__(self):
        self.min_heap = []  # larger half
        self.max_heap = []  # smaller half


    def addNum(self, num: int) -> None:
        if not self.max_heap:
            self.max_heap.append(-num)
            return

        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        while abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                num_to_move = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num_to_move)
            else:
                num_to_move = -heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, num_to_move)
        

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        