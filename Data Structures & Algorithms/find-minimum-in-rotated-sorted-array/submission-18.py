class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]  #1
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                ans = min(ans, nums[l])
                break
            
            mid = (l+r)//2
            ans = min(ans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid-1

        return ans