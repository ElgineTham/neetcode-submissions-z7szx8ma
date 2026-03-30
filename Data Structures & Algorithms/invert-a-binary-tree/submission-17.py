# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            
            temp = root.left
            root.left = root.right
            root.right = temp
            dfs(root.left)
            dfs(root.right)
        
        q = deque([root])
        if not root:
            return None
        def bfs(root):
            while q:
                node = q.popleft()
                node.left, node.right = node.right, node.left

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        bfs(root)
        return root