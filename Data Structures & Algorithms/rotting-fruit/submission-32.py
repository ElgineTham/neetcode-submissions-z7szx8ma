class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0

        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        q.append((nr, nc))

            time += 1

        return time if not fresh else -1