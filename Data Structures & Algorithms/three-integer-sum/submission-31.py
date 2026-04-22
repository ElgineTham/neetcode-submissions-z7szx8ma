class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            m, r = i+1, len(nums)-1
            while m < r:
                total = nums[i] + nums[m] + nums[r]
                if total < 0:
                    m += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
        
        return ans