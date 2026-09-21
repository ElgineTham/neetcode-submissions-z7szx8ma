# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:   
        if p.val > q.val:
            temp = p
            p = q
            q = temp
             
        def dfs(root, p, q):
            if not root:
                return
            
            if p.val <= root.val <= q.val:
                return root
            elif p.val <= root.val and q.val <= root.val:
                return dfs(root.left, p, q)
            else:
                return dfs(root.right, p, q)
            
        return dfs(root, p, q)