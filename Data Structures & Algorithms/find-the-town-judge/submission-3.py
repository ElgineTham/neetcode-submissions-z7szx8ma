class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town_map = [[0,0] for i in range(n+1)]
        for a, b in trust:
            town_map[a][0] += 1
            town_map[b][1] += 1
        
        for i in range(1, n+1):
            if town_map[i][0] == 0 and town_map[i][1] == n-1:
                return i

        return -1