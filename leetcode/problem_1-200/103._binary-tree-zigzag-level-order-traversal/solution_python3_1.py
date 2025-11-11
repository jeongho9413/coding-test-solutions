"""
leetcode - 103. binary tree zigzag level order traversal
using a bfs with a deque
time: O(n)
space: O(w)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #
        if not root:
            return []

        #
        res = list()
        q = deque([root])
        flag = False

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

            if not flag:
                res.append(same_level)
            else:
                res.append(same_level[::-1])
            flag = not flag

        return res
