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
        def bfs(root):
            while q:
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    temp = node.left
                    node.left = node.right
                    node.right = temp

        bfs(root)
        return root