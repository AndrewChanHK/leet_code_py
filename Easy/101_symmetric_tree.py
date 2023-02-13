# 101. Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left)

        return p is q

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.isSame(root.left, root.right)
