class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = defaultdict(list)
        for src, dst in edges:
            edgeMap[dst].append(src)
            edgeMap[src].append(dst)
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return
            
            visit.add(node)
            for nei in edgeMap[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

            return
        
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
            dfs(i, i-1)
        
        return count