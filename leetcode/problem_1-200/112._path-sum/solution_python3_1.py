# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        #
        def dfs(node, global_sum):
            if not node:
                return False
            if not node.left and not node.right:
                return global_sum - node.val == 0

            global_sum -= node.val

            sum_left = dfs(node.left, global_sum)
            sum_right = dfs(node.right, global_sum)

            return sum_left or sum_right

        #
        return dfs(root, targetSum)
