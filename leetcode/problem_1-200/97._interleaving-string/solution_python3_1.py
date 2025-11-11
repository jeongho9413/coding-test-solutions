"""
leetcode - 97. interleaving string
using a dfs with top-down dp
time: O(n1 * n2)
space: O(n1 * n2)
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        #
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        #
        if n1 + n2 != n3:
            return False

        cache = [[None] * (n2 + 1) for _ in range(n1 + 1)]

        #
        def dfs(i, j):
            if i == n1 and j == n2:
                return True
            if cache[i][j] is not None:
                return cache[i][j]

            k = i + j
            ok = False

            if i < n1 and s1[i] == s3[k] and dfs(i + 1, j):
                ok = True
            if not ok and j < n2 and s2[j] == s3[k] and dfs(i, j + 1):
                ok = True

            cache[i][j] = True if ok else False
            return cache[i][j]

        #
        return dfs(0, 0)
