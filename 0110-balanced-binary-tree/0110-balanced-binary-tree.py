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
        return (self.get_height(root)>=0)
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node or None:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        
        if left < 0 or right < 0 or abs(left - right) > 1: 
            return -1
        
        return max(left,right) + 1
        