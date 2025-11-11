# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        #
        postorder = deque(postorder)

        #
        def dfs(inorder, postorder):
            if not inorder:
                return None

            i = inorder.index(postorder.pop())  # O(n) time
            node = TreeNode(inorder[i])
            node.right = dfs(inorder[i + 1:], postorder)
            node.left = dfs(inorder[:i], postorder)
            return node

        #
        return dfs(inorder, postorder)
