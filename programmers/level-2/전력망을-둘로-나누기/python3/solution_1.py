# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# strategy: brute-force with bfs
# time: O(N^2)
# space: O(N)
from collections import deque

def bfs(start, graph, n, v1, v2):
    cnt = 1
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    
    while q:
        curr = q.popleft()
        for neig in graph[curr]:
            if not visited[neig] and not (curr == v1 and neig == v2) and not (curr == v2 and neig == v1):
                visited[neig] = True
                q.append(neig)
                cnt += 1
    return cnt
                

def solution(n, wires):
    
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    res = n
    
    for v1, v2 in wires:
        cnt1 = bfs(v1, graph, n, v1, v2)
        cnt2 = n - cnt1
        res = min(res, abs(cnt1 - cnt2))
        
    return res
