class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        
        if k >= len(nums):
            return [max(nums)]

        l, r = 0, 0
        q = deque()
        while r - l < k:
            if not q:
                q.append((nums[r], r))
            else:
                while q and nums[r] > q[-1][0]:
                    q.pop()
                q.append((nums[r], r))
            
            r += 1
        
        ans = []
        r -= 1
        ans.append(q[0][0])

        while r < len(nums) - 1:
            l += 1
            r += 1

            if q[0][1] < l:
                q.popleft()

            if not q:
                q.append((nums[r], r))
            else:
                while q and nums[r] > q[-1][0]:
                    q.pop()
                q.append((nums[r], r))
            
            ans.append(q[0][0])
        
        return ans


