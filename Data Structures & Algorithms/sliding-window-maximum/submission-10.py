class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        heap = [-nums[i] for i in range(k)]
        heapq.heapify(heap)

        l, r = 0, k-1
        while r < len(nums):
            answer.append(-heap[0])
            heap.remove(-nums[l])
            heapq.heapify(heap)
            l += 1
            r += 1
            if r < len(nums):
                heapq.heappush(heap, -nums[r])
        
        return answer