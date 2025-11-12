class Solution:
    def rob(self, nums: List[int]) -> int:

        #
        n = len(nums)
        cache = [None] * (n + 1)

        #
        def dfs(i):
            if i >= n:
                return 0
            if cache[i] is not None:
                return cache[i]

            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]

        #
        return dfs(0)
