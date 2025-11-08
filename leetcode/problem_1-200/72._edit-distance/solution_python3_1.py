class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        #
        m = len(word1)
        n = len(word2)
        cache = [[None] * (n + 1) for _ in range(m + 1)]

        #
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if cache[i][j] is not None:
                return cache[i][j]

            if word1[i] == word2[j]:
                cache[i][j] = dfs(i + 1, j + 1)
            else:
                insert_cost = dfs(i, j + 1)
                delete_cost = dfs(i + 1, j)
                replace_cost = dfs(i + 1, j + 1)
                cache[i][j] = 1 + min(insert_cost, delete_cost, replace_cost)
                
            return cache[i][j]
        
        #
        return dfs(0, 0)
