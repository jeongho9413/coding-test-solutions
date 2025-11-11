"""
leetcode - 90. subset II
using backtracking
time: O(2^n * n)
space: O(n)
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        #
        res = list()
        nums.sort()

        #
        def dfs(i, comb):
            if i == len(nums):
                res.append(comb.copy())
                return

            comb.append(nums[i])
            dfs(i + 1, comb)
            comb.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, comb)

        #
        dfs(0, list())
        return res
