# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# strategy: bfs w/o visited
# time: O(N \times M)
# space: O(N \times M)
def solution(maps):
    
    from collections import deque
    
    n, m = len(maps), len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(0, 0)])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    res = maps[n - 1][m - 1]
    
    return res if res > 1 else -1
