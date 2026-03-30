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
        copy = {None: None}

        dummy = head
        while dummy:
            copyNode = Node(dummy.val)
            copy[dummy] = copyNode
            dummy = dummy.next
        
        dummy = head
        while dummy:
            copyNode = copy[dummy]
            copyNode.next = copy[dummy.next]
            copyNode.random = copy[dummy.random]
            dummy = dummy.next
        
        return copy[head]