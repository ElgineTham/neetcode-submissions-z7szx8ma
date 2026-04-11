# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy

        remainder = 0
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next
            
            total += remainder
            remainder = total // 10
            total %= 10

            curr.next = ListNode(total, None)
            curr = curr.next
        
        while remainder > 0:
            curr.next = ListNode(remainder%10, None)
            curr = curr.next
            remainder //= 10

        return dummy.next