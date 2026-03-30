# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root):
            if not root:
                return [True, 0]

            root.left = dfs(root.left)
            root.right = dfs(root.right)
            balanced = root.left[0] and root.right[0] and abs(root.left[1]-root.right[1]) < 2

            return [balanced, 1 + max(root.left[1], root.right[1])]
        
        return dfs(root)[0]