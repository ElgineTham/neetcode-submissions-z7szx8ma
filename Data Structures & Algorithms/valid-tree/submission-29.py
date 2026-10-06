class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        edge_map = defaultdict(list)
        for v1, v2 in edges:
            edge_map[v1].append(v2)
            edge_map[v2].append(v1)

        cycle = True
        def dfs(v1, parent):
            nonlocal cycle
            if v1 in visited:
                cycle = False
                return
            
            visited.add(v1)

            for v2 in edge_map[v1]:
                if v2 == parent:
                    continue
                dfs(v2, v1)
        
        dfs(0, None)
        return cycle and len(visited) == n
            
