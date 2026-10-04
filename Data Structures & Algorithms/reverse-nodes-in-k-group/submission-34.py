# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        prev_group = dummy

        while True:
            kth = prev_group
            i = 0
            while kth and i < k:
                kth = kth.next
                i += 1
            
            if not kth:
                break
            
            curr = prev_group.next
            prev = kth.next
            
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            new_tail = prev_group.next
            prev_group.next = kth
            prev_group = new_tail
        
        return dummy.next
            


