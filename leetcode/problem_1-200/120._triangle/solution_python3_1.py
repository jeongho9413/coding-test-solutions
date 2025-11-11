class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        #
        n = len(triangle)
        cache = [[None] * (r + 1) for r in range(n + 1)]

        #
        def dfs(r, c):
            if r == n - 1:
                return triangle[r][c]
            if cache[r][c] is not None:
                return cache[r][c]

            cache[r][c] = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
            return cache[r][c]

        #
        return dfs(0, 0)
