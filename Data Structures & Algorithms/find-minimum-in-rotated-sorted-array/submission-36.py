class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] < nums[r] or l == r:
            return nums[l]
        while l <= r:
            m = (l+r)//2
            if nums[m+1] < nums[m]:
                return nums[m+1]
            if nums[l] <= nums[m]:
                l = m+1
            elif nums[l] > nums[m]:
                r = m-1
        