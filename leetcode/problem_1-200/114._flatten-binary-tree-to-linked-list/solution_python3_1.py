# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        #
        if not root:
            return None

        #
        q = deque(list())

        #
        def preorder(node):
            if not node:
                return

            q.append(node)
            preorder(node.left)
            preorder(node.right)

        #
        preorder(root)
        root = q.popleft()
        while q:
            root.right = q.popleft()
            root.left = None
            root = root.right
