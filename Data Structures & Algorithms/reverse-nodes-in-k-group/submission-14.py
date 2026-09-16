# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groups = []
        dummy = head
        prev, aft = None, head
        while dummy:
            i = 0
            while i < k and aft:
                prev = aft
                aft = aft.next
                i += 1
            
            prev.next = None
            groups.append([dummy, i])
            dummy = aft

        for i, content in enumerate(groups):
            group, length = content
            if length == k:
                first = group
                dummy1 = group
                prev = None
                while dummy1:
                    temp = dummy1.next
                    dummy1.next = prev
                    prev = dummy1
                    dummy1 = temp
            
                groups[i] = [prev, first]
        
        for i in range(len(groups)):
            if i + 1 < len(groups):
                groups[i][1].next = groups[i+1][0]
        
        return groups[0][0]


