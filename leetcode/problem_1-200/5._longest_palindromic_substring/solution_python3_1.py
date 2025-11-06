class Solution:
    def longestPalindrome(self, s: str) -> str:

        #
        n = len(s)
        cache = [[None] * (n + 1) for _ in range(n + 1)]

        #
        def dfs(l, r):
            if l >= r:
                return 1

            if cache[l][r] is not None:
                return cache[l][r]
            
            if s[l] != s[r]:
                return 0
            else:
                cache[l][r] = dfs(l + 1, r - 1)
                return cache[l][r]

        #
        best_len = 1
        best_l = 0

        for i in range(n):
            for j in range(i + 1, n):
                if j - i + 1 <= best_len:
                    continue
                
                if dfs(i, j) == 1:
                    best_len = j - i + 1
                    best_l = i

        return s[best_l : best_l + best_len]
