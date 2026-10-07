class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        components = 0
        seen = set()
        def dfs(v1, parent):
            if v1 in seen:
                return
            
            seen.add(v1)

            for v2 in adj[v1]:
                if v2 == parent:
                    continue
                dfs(v2, v1)
        
        for i in range(n):
            if i not in seen:
                dfs(i, None)
                components += 1
        
        return components