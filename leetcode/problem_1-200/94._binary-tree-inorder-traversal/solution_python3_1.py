"""
leetcode - 94. binary tree inorder traversal
using an inorder traversal
time: O(n)
space: O(log n)-O(h)-O(n) where h is the height of a binary tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #
        res = list()

        #
        def inorder(node, arr):
            if not node:
                return

            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        #
        inorder(root, res)
        return res
