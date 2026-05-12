# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# strategy: bfs with cache and iteration
# time: O(n^2)
# space: O(n)
def solution(n, computers):
    
    res = 0
    visited = [False] * n
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            res += 1
            
    return res
