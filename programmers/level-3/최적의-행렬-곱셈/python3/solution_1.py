# https://school.programmers.co.kr/learn/courses/30/lessons/12942
# Strategy: Top-down DP with memoization
# Time: O(n^3)
# Space: O(n^2)
def solution(matrix_sizes):
    n = len(matrix_sizes)
    
    cache = [[None] * (n + 1) for _ in range(n + 1)]
    
    def dfs(i, j):
        if i == j:
            return 0
        
        if cache[i][j] is not None:
            return cache[i][j]
        
        min_cost = float('inf')
        
        for k in range(i, j):
            cost = (dfs(i, k) + dfs(k + 1, j) + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
            
            min_cost = min(min_cost, cost)
            
        cache[i][j] = min_cost
        return cache[i][j]
    
    return dfs(0, n - 1)
