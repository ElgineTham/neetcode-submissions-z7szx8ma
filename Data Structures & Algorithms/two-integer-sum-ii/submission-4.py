class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []

        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] == target:
                answer = [l+1, r+1]
                break
        
        return answer