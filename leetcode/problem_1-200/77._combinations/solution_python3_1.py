"""
leetcode - 77. combinations
using a backtracking
time: O(n C k * k)
space: O(k)
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        #
        res = list()

        #
        def dfs(i, comb):
            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())
                return

            comb.append(i)
            dfs(i + 1, comb)
            comb.pop()
            dfs(i + 1, comb)

        #
        dfs(1, list())
        return res
