# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        a = self.get_height(root)
        return a
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        lheight = self.get_height(node.left)
        rheight = self.get_height(node.right)
        
        return max(lheight,rheight) + 1
        