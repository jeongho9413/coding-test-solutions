class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #
        m = len(board)
        n = len(board[0])
        visited = set()

        #
        def surround(i, j):
            return 0 < i < m - 1 and 0 < j < n - 1

        #
        def dfs(i, j, mp, visited):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if (i, j) in visited or board[i][j] == "X":
                return

            mp.append((i, j))
            visited.add((i, j))
            dfs(i - 1, j, mp, visited)
            dfs(i + 1, j, mp, visited)
            dfs(i, j - 1, mp, visited)
            dfs(i, j + 1, mp, visited)

        #
        for i in range(m):
            for j in range(n):
                if (i, j) in visited or board[i][j] != "O":
                    continue
                
                mp = list()
                dfs(i, j, mp, visited)
                flip = all(surround(r, c) for (r, c) in mp)
                if flip:
                    for (r, c) in mp:
                        board[r][c] = "X"
