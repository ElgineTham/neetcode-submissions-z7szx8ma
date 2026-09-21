# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(min_val, node, max_val):
            if not node:
                return True
            
            if min_val >= node.val or max_val <= node.val:
                return False
            
            return (check(min_val, node.left, node.val)
                    and check(node.val, node.right, max_val))
        
        return check(float("-inf"), root, float("inf"))