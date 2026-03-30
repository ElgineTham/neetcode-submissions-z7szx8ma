# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p, q])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if t1 is None and t2 is not None:
                return False
            if t1 is not None and t2 is None:
                return False
            if t1 and t2 and t1.val != t2.val:
                return False
            
            if t1:
                queue.append(t1.left)
            if t2:
                queue.append(t2.left)
            if t1:
                queue.append(t1.right)
            if t2:
                queue.append(t2.right)
        
        return True