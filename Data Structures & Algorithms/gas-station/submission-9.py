class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = 0, 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
        
        if total_gas < total_cost:
            return -1
        
        total = 0
        result = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                result = i+1
        
        return result