# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy.next
        length = 0
        while curr:
            length += 1
            curr = curr.next

        prev, node_to_remove = dummy, dummy.next
        for i in range(length-n):
            prev = node_to_remove
            node_to_remove = node_to_remove.next
        
        prev.next = node_to_remove.next

        return dummy.next