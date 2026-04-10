class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        l, r = 0, 0
        curr_max = [-1, -1] # [idx, max_val]
        while r < k:
            if curr_max[1] < nums[r]:
                curr_max = [r, nums[r]]
            r += 1
        
        answer.append(curr_max[1])
        r = k-1

        while r < len(nums)-1:
            l += 1
            r += 1

            if nums[r] > curr_max[1]:
                curr_max = [r, nums[r]]
                answer.append(curr_max[1])
            elif l < curr_max[0]:
                answer.append(curr_max[1])
            else: 
                max_val = [-1, -1]
                for m in range(l, r+1):
                    if max_val[1] < nums[m]:
                        max_val = [m, nums[m]]
                curr_max = max_val
                answer.append(curr_max[1])

        return answer

                
        
        
        