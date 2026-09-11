# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged = self.mergeList(l1, l2)
                merged_lists.append(merged)
            
            lists = merged_lists
        
        return lists[0]
    
    def mergeList(self, l1, l2):
        answer = ListNode()
        dummy = answer

        while l1 or l2:
            if not l1:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
            elif not l2:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
        
        return answer.next