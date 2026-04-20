class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        ans = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[1] < newInterval[0]:
                ans.append(curr)
            elif curr[0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            else:
                curr[0] = min(curr[0], newInterval[0])
                curr[1] = max(curr[1], newInterval[1])
                for j in range(i+1, len(intervals)):
                    n = intervals[j]
                    if curr[1] < n[0]:
                        ans.append(curr)
                        return ans + intervals[j:]
                    else:
                        curr[0] = min(curr[0], n[0])
                        curr[1] = max(curr[1], n[1])
                ans.append(curr)
                return ans
        
        ans.append(newInterval)
        return ans