# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        answer = ListNode(val=0, next=None)
        dummy = answer
        while l1 or l2:
            if not l1:
                total = l2.val + remainder
                remainder = total // 10
                total %= 10
                dummy.next = ListNode(val=total)
                l2 = l2.next
                dummy = dummy.next
            elif not l2:
                total = l1.val + remainder
                remainder = total // 10
                total %= 10
                dummy.next = ListNode(val=total)
                l1 = l1.next
                dummy = dummy.next
            else:
                total = l1.val + l2.val + remainder
                remainder = total // 10
                total %= 10
                dummy.next = ListNode(val=total)
                dummy = dummy.next
                l1 = l1.next
                l2 = l2.next
        
        while remainder:
            dummy.next = ListNode(val=remainder%10)
            remainder //= 10
            dummy = dummy.next
        
        return answer.next
