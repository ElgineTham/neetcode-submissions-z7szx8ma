class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        done = set()
        answer = []
        m, r = 0, 0
        for l in range(length-2):
            if nums[l] is None or nums[l] in done:
                continue
            else:
                done.add(nums[l])
                m = l+1
                r = len(nums)-1
                while m < r:
                    threeSum = nums[l]+nums[m]+nums[r]
                    if threeSum < 0:
                        m += 1
                    elif threeSum > 0:
                        r -= 1
                    elif threeSum == 0:
                        answer.append([nums[l],nums[m],nums[r]])
                        m += 1
                        while m < r and nums[m] == nums[m-1]:
                            m += 1
        
        return answer

        