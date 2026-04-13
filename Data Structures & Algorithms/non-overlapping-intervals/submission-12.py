class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end <= intervals[i][0]:
                prev_end = intervals[i][1]
            else:
                res += 1
                prev_end = min(prev_end, intervals[i][1])
        
        return res