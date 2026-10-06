class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        edge_map = defaultdict(list)
        for v1, v2 in edges:
            edge_map[v1].append(v2)
            edge_map[v2].append(v1)

        def dfs(v1, parent):
            if v1 in visited:
                return False
            
            visited.add(v1)

            for v2 in edge_map[v1]:
                if v2 == parent:
                    continue
                if not dfs(v2, v1):
                    return False
            return True
        
        return dfs(0, None) and len(visited) == n
            
