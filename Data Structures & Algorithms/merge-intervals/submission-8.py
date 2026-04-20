class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort()
        last = intervals[0]

        ans = []
        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] > last[1]:
                ans.append(last)
                last = curr
            else:
                last[1] = max(last[1], curr[1])

        ans.append(last)
        return ans
