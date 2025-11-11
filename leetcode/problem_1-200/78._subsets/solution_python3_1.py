"""
leetcode - 78. subsets
using a backtracking
time: O(2^n * n)
space: O(n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #
        res = list()

        #
        def dfs(i, comb):
            if i == len(nums):
                res.append(comb.copy())
                return

            comb.append(nums[i])
            dfs(i + 1, comb)
            comb.pop()
            dfs(i + 1, comb)

        #
        dfs(0, list())
        return res
