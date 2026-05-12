# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# strategy: DFS with Eulerian path
# time: O(N log N)
# space: O(N)
from collections import defaultdict

def solution(tickets):
    
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
        
    for key in graph:
        graph[key].sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        
        if top in graph and graph[top]:
            stack.append(graph[top].pop())  # O(1)
        else:
            path.append(stack.pop())
            
    return path[::-1]
