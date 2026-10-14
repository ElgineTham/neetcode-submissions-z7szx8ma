class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_time = float("inf")
        seen = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        heap = [[grid[0][0], 0, 0]]

        while heap:
            cost, r, c = heapq.heappop(heap)
            if (r, c) == (rows-1, cols-1):
                return min(min_time, cost)
            
            if (r, c) in seen:
                continue
            
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols
                    or (nr, nc) in seen):
                    continue

                ncost = max(cost, grid[nr][nc])
                heapq.heappush(heap, [ncost, nr, nc])
