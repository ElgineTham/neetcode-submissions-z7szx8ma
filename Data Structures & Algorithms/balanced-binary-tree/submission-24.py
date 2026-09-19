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

        def check_subtree(root):
            if not root:
                return [True, 0]
            
            left = check_subtree(root.left)
            right = check_subtree(root.right)
            balanced = (left[0] and right[0] and 
                        (abs(left[1]-right[1]) <= 1))
            max_height = max(left[1], right[1])

            return [balanced, 1 + max_height]

        left = check_subtree(root.left)
        right = check_subtree(root.right)

        return (left[0] and right[0] and 
                (abs(left[1]-right[1]) <= 1))
        
        
        
