class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        value = self.time_map[key]
        l, r = 0, len(value) - 1
        largest_m = -1
        while l <= r:
            m = (l + r) // 2
            if value[m][1] <= timestamp:
                largest_m = max(largest_m, m)
                l = m + 1
            else:
                r = m - 1
        
        if largest_m == -1:
            return ""
        else:
            return value[largest_m][0]
            
        
