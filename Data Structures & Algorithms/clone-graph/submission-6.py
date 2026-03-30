"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}

        def dfs(cur):
            if cur in copy:
                return copy[cur]
            
            createCopy = Node(cur.val)
            copy[cur] = createCopy
            for neighbor in cur.neighbors:
                createCopy.neighbors.append(dfs(neighbor))
            return createCopy
        
        return dfs(node) if node else None