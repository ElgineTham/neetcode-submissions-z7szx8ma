class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        longest = 0
        for i in range(len(nums)):
            numSet.add(nums[i])
        for number in numSet:
            curr_num = number
            if curr_num - 1 not in numSet:
                sequence = 1
                while curr_num + 1 in numSet:
                    sequence += 1
                    curr_num += 1
                longest = max(longest,sequence)
        
        return longest

        