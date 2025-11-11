"""
leetcode - 101. symmetric tree
using a dfs
time: O(n)
space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        #
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            val = (p.val == q.val)
            left = dfs(p.left, q.right)
            right = dfs(p.right, q.left)
            return val and left and right

        #
        return dfs(root.left, root.right)
