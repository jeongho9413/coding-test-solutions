class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        #
        if numRows <= 0:
            return []

        #
        res = list()
        cache = [[None] * (r + 1) for r in range(numRows)]

        #
        def dfs(r, c):
            if c == 0 or c == r:
                return 1
            if cache[r][c] is not None:
                return cache[r][c]

            cache[r][c] = dfs(r - 1, c - 1) + dfs(r - 1, c)
            return cache[r][c]

        #
        for r in range(numRows):
            temp = list()
            for c in range(r + 1):
                temp.append(dfs(r, c))
            res.append(temp)
        
        return res
