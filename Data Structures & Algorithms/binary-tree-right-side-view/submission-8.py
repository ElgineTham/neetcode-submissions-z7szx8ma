# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        q = deque()

        if root:
            q.append(root)
        
        while q:
            length = len(q)
            for _ in range(length - 1):
                curr_node = q.popleft()
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            
            curr_node = q.popleft()
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            answer.append(curr_node.val)
        
        return answer