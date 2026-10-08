class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        seen = set()

        def has_cycle(vertex, parent):
            if vertex in seen:
                return True
            
            seen.add(vertex)
            
            for nei in adj[vertex]:
                if nei == parent:
                    continue

                if has_cycle(nei, vertex):
                    return True
            
            seen.remove(vertex)
            return False
        
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

            if has_cycle(v1, None):
                return [v1, v2]