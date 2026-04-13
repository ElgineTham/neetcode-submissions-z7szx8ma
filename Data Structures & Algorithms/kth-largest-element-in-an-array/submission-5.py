class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-num for num in nums]
        heapq.heapify(arr)
        for i in range(k-1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)
