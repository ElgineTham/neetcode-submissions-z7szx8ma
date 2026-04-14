# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(low, root, high):
            if not root:
                return True
            
            if low < root.val < high:
                return dfs(low, root.left, root.val) and dfs(root.val, root.right, high)
            
            return False
        
        return dfs(float("-inf"), root, float("inf"))
