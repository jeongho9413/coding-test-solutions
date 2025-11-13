"""
leetcode - 5. longest palindromic substring
approach: using a dfs
time: O(n^2)
space: O(n^2)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        #
        n = len(s)
        cache = [[None] * (n + 1) for _ in range(n + 1)]

        #
        def dfs(l, r):
            if l >= r:
                return True
            if cache[l][r] is not None:
                return cache[l][r]
            
            if s[l] != s[r]:
                return False
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
                if dfs(i, j) == True:
                    best_len = j - i + 1
                    best_l = i

        return s[best_l : best_l + best_len]
