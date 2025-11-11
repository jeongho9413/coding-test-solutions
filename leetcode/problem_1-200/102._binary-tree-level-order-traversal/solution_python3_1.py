"""
leetcode - 102. binary tree level order traversal
using a bfs with deque
time: O(n)
space: O(w) where w is the maximum width of the given tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #
        if not root:
            return []

        #
        res = list()
        q = deque([root])

        #
        while q:
            same_level = list()
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                same_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(same_level)

        return res
