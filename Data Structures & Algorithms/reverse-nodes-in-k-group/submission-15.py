# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_kth_node(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1

        return node