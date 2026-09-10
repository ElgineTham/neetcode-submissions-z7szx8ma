# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2, d3 = list1, list2, ListNode()
        dummy = d3

        while d1 or d2:
            if not d1:
                d3.next = d2
                d2 = d2.next
                d3 = d3.next
            elif not d2:
                d3.next = d1
                d1 = d1.next
                d3 = d3.next
            else:
                if d1.val <= d2.val:
                    d3.next = d1
                    d1 = d1.next
                else:
                    d3.next = d2
                    d2 = d2.next
                
                d3 = d3.next

        return dummy.next