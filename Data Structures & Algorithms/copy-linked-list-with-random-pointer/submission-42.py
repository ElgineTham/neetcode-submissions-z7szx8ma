"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        old_node = head
        hash_map = {}

        while old_node:
            new_node = Node(old_node.val)
            hash_map[old_node] = new_node
            old_node = old_node.next
        
        old_node = head
        while old_node:
            new_node = hash_map[old_node]
            if not old_node.next:
                new_node.next = None
            else:
                new_node.next = hash_map[old_node.next]
            
            if not old_node.random:
                new_node.random = None
            else:
                new_node.random = hash_map[old_node.random]
            
            old_node = old_node.next
        
        return hash_map[head]
        