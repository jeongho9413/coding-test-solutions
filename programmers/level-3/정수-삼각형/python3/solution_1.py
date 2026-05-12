# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# Strategy: Bottom-up DP with optimal substructure and in-place modification
# Time: O(n^2)
# Space: O(1)
def solution(triangle):
    
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
            
    return triangle[0][0]
