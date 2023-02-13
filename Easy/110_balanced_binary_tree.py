# 110. Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return 0

        l = self.dfs(node.left)

        if l == -1:
            return -1

        r = self.dfs(node.right)

        if r == -1:
            return -1

        if abs(l-r) > 1:
            return -1

        return 1+max(l, r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
