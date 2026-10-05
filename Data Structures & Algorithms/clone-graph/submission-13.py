"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy_map = {}

        def dfs(cur):
            if cur in copy_map:
                return copy_map[cur]
            
            copy_map[cur] = Node(cur.val)
            copy_node = copy_map[cur]
            for nei in cur.neighbors:
                copy_node.neighbors.append(dfs(nei))
            
            return copy_node
        
        if node:
            return dfs(node)
        
        return None