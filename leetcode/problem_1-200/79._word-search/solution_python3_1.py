"""
leetcode - 79. word search
using a dfs
time: O(m * n * 4^L) where L is the length of the word
space: O(L)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #
        m = len(board)
        n = len(board[0])

        #
        def dfs(i, j, k):
            if k == len(word):
                return True
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "."

            right = dfs(i + 1, j, k + 1)
            left = dfs(i - 1, j, k + 1)
            top = dfs(i, j + 1, k + 1)
            bottom = dfs(i, j - 1, k + 1)

            if right or left or top or bottom:
                return True

            board[i][j] = temp
            return False

        #
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
