# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# Strategy: Floyd-Warshall algorithm / Graph
# Time: O(n^2)
# Space: O(n^2)
def solution(n, results):
    
    matrix = [[False] * (n + 1) for _ in range(n + 1)]
    
    for w, l in results:
        matrix[w][l] = True
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = True
                    
    res = 0
    
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if matrix[i][j] or matrix[j][i]:
                cnt += 1
                
        if cnt == n - 1:
            res += 1
            
    return res
