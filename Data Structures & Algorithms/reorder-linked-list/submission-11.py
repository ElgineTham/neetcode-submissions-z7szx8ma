# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next=head)
        first_half, second_half = dummy, dummy
        while second_half and second_half.next:
            first_half = first_half.next
            second_half = second_half.next.next

        second_half = first_half.next
        first_half.next = None
        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        dummy, answer = head, head
        while prev:
            temp1, temp2 = dummy.next, prev.next
            dummy.next = prev
            prev.next = temp1
            dummy = temp1
            prev = temp2