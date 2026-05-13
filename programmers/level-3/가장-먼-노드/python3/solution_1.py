# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# Strategy: Graph with BFS
# Time: O(V + E)
# Space: O(V + E)
from collections import deque

def solution(n, edge):
    graph = [list() for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    distances = [-1] * (n + 1)
    q = deque([1])
    distances[1] = 0
    
    while q:
        curr = q.popleft()
        
        for neig in graph[curr]:
            if distances[neig] == -1:
                distances[neig] = distances[curr] + 1
                q.append(neig)
                
    max_dist = max(distances)
    
    return distances.count(max_dist)
