# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# strategy: MST(Minimum Spanning Tree) -> Kruskal algorithm with Union-Find (based on Greedy)
# time: O(E log E)
# space: O(N)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    total_cost = 0
    edges_count = 0
    
    for v1, v2, cost in costs:
        if find(parent, v1) != find(parent, v2):
            union(parent, v1, v2)
            total_cost += cost
            edges_count += 1
            
            if edges_count == n - 1:
                break
                
    return total_cost
