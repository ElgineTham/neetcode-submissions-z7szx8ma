class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []

        for l in range(len(nums)-2):
            if l-1 >= 0 and nums[l] == nums[l-1]:
                continue
            else:
                m = l+1
                r = len(nums)-1
                while m < r:
                    total = nums[l] + nums[m] + nums[r]
                    if total < 0:
                        m += 1
                    elif total > 0:
                        r -= 1
                    elif total == 0:
                        answer.append([nums[l], nums[m], nums[r]])
                        m += 1
                        while m < r and nums[m] == nums[m-1]:
                            m += 1
        
        return answer