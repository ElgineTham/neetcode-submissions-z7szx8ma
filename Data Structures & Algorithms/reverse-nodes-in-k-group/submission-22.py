class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(group_prev, k):
            for i in range(k):
                if not group_prev:
                    return None
                group_prev = group_prev.next
            return group_prev
        
        dummy = ListNode(next=head)
        group_prev = dummy

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break

            prev = kth.next
            curr = group_prev.next
            
            # Save reference to the node that will become the group tail
            group_tail = group_prev.next
            
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            group_prev.next = kth
            group_prev = group_tail  # ✅ Correct: Advance group_prev to the tail of this group

        return dummy.next

