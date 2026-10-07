class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edgeMap = {edge+1: [] for edge in range(len(edges))}
        
        cycle = set()
        def dfs(node, parent):
            if node in cycle:
                return True
            
            cycle.add(node)
            for nei in edgeMap[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            cycle.remove(node)

            return False
        
        for src, dst in edges:
            edgeMap[src].append(dst)
            edgeMap[dst].append(src)
            if dfs(src, -1):
                return [src, dst]


