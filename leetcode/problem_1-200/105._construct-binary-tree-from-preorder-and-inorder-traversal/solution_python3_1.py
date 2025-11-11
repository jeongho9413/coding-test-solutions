# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        #
        preorder = deque(preorder)

        #
        def dfs(inorder, preorder):
            if not inorder:
                return None

            i = inorder.index(preorder.popleft())  # O(n) time
            node = TreeNode(inorder[i])
            node.left = dfs(inorder[:i], preorder)
            node.right = dfs(inorder[i + 1:], preorder)
            return node

        #
        return dfs(inorder, preorder)
