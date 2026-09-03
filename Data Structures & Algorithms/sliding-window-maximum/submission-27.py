class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        
        if k >= len(nums):
            return [max(nums)]
        
        l, r = 0, 0
        largest = float("-inf")
        ind = -1

        ans = []

        while r-l < k:
            if nums[r] > largest:
                largest = nums[r]
                ind = r
            r += 1

        ans.append(largest)
        r -= 1
        
        while r < len(nums) - 1:
            l += 1
            r += 1
            if nums[r] > largest:
                largest = nums[r]
                ind = r
            
            if ind < l:
                temp = l
                largest = float("-inf")
                while temp <= r:
                    if nums[temp] > largest:
                        largest = nums[temp]
                        ind = temp
                    temp += 1
                
            ans.append(largest)
        
        return ans