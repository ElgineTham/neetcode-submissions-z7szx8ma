class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_map = defaultdict(list)

        for src, dst in edges:
            edge_map[src].append(dst)
            edge_map[dst].append(src)

        min_height, ans = float("inf"), []
        for i in range(n):
            q = deque()
            q.append(i)
            seen = set()
            height = 0

            while q:
                for j in range(len(q)):
                    node = q.popleft()
                    seen.add(node)
                    for nei in edge_map[node]:
                        if nei in seen:
                            continue
                        else:
                            q.append(nei)
                
                if q:
                    height += 1
            
            if min_height == height:
                ans.append(i)
            if min_height > height:
                min_height = height
                ans = [i]
        
        return ans


