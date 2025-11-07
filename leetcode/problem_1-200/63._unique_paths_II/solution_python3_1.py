class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        #
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = [[None] * (n + 1) for _ in range(m + 1)]

        #
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if cache[r][c] is not None:
                return cache[r][c]

            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]

        #
        return dfs(0, 0)
