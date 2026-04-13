class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort()
        res = 0
        curr_interval = intervals[0]

        for i in range(1, len(intervals)):
            if curr_interval[1] <= intervals[i][0]:
                curr_interval = intervals[i]
            elif curr_interval[0] >= intervals[i][1]:
                continue
            else:
                res += 1
                if curr_interval[1] < intervals[i][1]:
                    continue
                else:
                    curr_interval = intervals[i]
        
        return res