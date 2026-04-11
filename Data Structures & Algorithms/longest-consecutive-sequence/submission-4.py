class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = set()
        longest = 0

        for num in nums:
            num_map.add(num)
        
        for num in num_map:
            if num-1 not in num_map:
                sequence = 1
                while num+1 in num_map:
                    sequence += 1
                    num += 1
                
                longest = max(longest, sequence)

        return longest