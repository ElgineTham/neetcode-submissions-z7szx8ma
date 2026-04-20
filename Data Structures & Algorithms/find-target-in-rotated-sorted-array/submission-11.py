class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: #sorted
                if nums[l] <= target and nums[mid] >= target: #between l and mid
                    r = mid-1
                else:
                    l = mid+1
            else: #unsorted
                if (nums[l] <= target and nums[mid] <= target) or (nums[l] >= target and nums[mid] >= target): #between l and mid
                    r = mid-1
                else:
                    l = mid+1
        
        return -1