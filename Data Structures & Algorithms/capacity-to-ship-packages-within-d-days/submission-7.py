class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)

        l, r = max(weights), sum(weights)
        least_weight = sum(weights)

        while l <= r:
            window, time = 0, 0
            m = (l+r)//2

            for weight in weights:
                if window + weight <= m:
                    window += weight
                else:
                    time += 1
                    window = weight
            time += 1

            if time <= days:
                least_weight = min(least_weight, m)
                r = m-1
            else:
                l = m+1
        
        return least_weight
