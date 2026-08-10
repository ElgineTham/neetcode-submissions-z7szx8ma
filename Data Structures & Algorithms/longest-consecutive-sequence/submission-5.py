class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        longest = 0
        for num in seen:
            if num-1 not in seen:
                sequence = 1
                while num+1 in seen:
                    sequence += 1
                    num += 1
                
                longest = max(longest, sequence)
        
        return longest