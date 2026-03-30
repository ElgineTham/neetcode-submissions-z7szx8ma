class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        answer = []
        while len(answer) < k:
            curr_max = float("-inf")
            curr_key = 0
            for key, values in count.items():
                if curr_max < values:
                    curr_key = key
                    curr_max = values
            answer.append(curr_key)
            count.pop(curr_key)
        return answer