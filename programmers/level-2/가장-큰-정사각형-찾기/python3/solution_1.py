# https://school.programmers.co.kr/learn/courses/30/lessons/12905
# Strategy: top-down DP with memoization/caching
# Time: O(row \times col)
# Space: O(row \times col)
def solution(board):
    row, col = len(board), len(board[0])

    cache = [[None] * (col + 1) for _ in range(row + 1)]
    
    def dfs(r, c):
        if r < 0 or c < 0:
            return 0
        
        if board[r][c] == 0:
            return 0
        
        if cache[r][c] is not None:
            return cache[r][c]
        
        up = dfs(r - 1, c)
        left = dfs(r, c - 1)
        diag = dfs(r - 1, c - 1)
        
        cache[r][c] = min(up, left, diag) + 1
        
        return cache[r][c]
    
    max_side = 0
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                max_side = max(max_side, dfs(i, j))
                
    return max_side ** 2
