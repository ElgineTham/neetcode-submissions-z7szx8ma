class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        answer = []
        for i in range(k):
            curr_freq = float("-inf")
            curr_val = 0
            for key in count:
                if count[key] >= curr_freq:
                    curr_freq = count[key]
                    curr_val = key
                    
            answer.append(curr_val)
            count.pop(curr_val)
        
        return answer