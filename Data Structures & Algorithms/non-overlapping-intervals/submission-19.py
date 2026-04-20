class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort()

        count = 0
        last = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]

            if last[1] > curr[0]:
                count += 1
                if last[1] > curr[1]:
                    last = curr
            else:
                last = curr
        
        return count