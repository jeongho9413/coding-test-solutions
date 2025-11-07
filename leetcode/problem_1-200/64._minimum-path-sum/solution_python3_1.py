class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        #
        m = len(grid)
        n = len(grid[0])
        cache = [[None] * (n + 1) for _ in range(m + 1)]

        #
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if cache[r][c] is not None:
                return cache[r][c]

            min_val = float('inf')
            if r < m - 1:
                min_val = min(min_val, dfs(r + 1, c))
            if c < n - 1:
                min_val = min(min_val, dfs(r, c + 1))

            cache[r][c] = grid[r][c] + min_val
            return cache[r][c]

        #
        return dfs(0, 0)
