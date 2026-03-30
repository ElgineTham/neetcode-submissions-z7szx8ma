# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        value = l1.val + l2.val
        remainder = value // 10
        value %= 10
        dummy = ListNode(value)
        pointer = dummy
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            value = l1.val + l2.val + remainder
            remainder = 0
            if value > 9:
                remainder = value // 10
                value %= 10
            dummy.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        while remainder or l1 or l2:
            value = 0
            if not l1 and not l2:
                dummy.next = ListNode(remainder)
                remainder = 0
            else:
                if l1:
                    value = l1.val
                    l1 = l1.next
                if l2:
                    value = l2.val
                    l2 = l2.next
                value += remainder
                remainder = 0
                if value > 9:
                    remainder = value // 10
                    value %= 10
                dummy.next = ListNode(value)
                dummy = dummy.next

        return pointer
        


        