class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #
        hs = set(wordDict)
        n = len(s)
        cache = [None] * (n + 1)

        #
        def dfs(i):
            if i == n:
                return True
            if cache[i] is not None:
                return cache[i]

            for j in range(i + 1, n + 1):
                if s[i : j] in hs and dfs(j):
                    cache[i] = True
                    return cache[i]

            cache[i] = False
            return cache[i]

        #
        return dfs(0)
