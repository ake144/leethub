# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if not root:
            return 
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            poped = stack.pop()
            res.append(poped.val)
            root = poped.right
        return res