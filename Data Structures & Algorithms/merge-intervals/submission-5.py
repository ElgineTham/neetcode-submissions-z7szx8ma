class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_interval = intervals[0]
        res = []
        
        for i in range(1, len(intervals)):
            if curr_interval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif curr_interval[1] < intervals[i][0]:
                res.append(curr_interval)
                curr_interval = intervals[i]
            else:
                curr_interval = [min(curr_interval[0], intervals[i][0]), max(curr_interval[1], intervals[i][1])] 

        res.append(curr_interval)
        return res