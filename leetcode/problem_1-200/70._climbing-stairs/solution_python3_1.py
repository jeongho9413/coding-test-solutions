class Solution:
    def climbStairs(self, n: int) -> int:

        #
        cache = [None] * (n + 1)
        
        #
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] is not None:
                return cache[i]
            
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        #
        return dfs(0)
