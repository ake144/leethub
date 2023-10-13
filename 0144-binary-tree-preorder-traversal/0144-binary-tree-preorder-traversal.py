# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            poped = stack.pop()
            res.append(poped.val)
            if poped.right:
                stack.append(poped.right)
            
            if poped.left:
                stack.append(poped.left)
        return res
        