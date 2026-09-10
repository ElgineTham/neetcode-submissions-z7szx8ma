# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 0
        dummy = head
        while dummy:
            total_length += 1
            dummy = dummy.next
        
        if n == total_length:
            return head.next
        
        prev, curr = None, head
        for i in range(total_length - n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return head
