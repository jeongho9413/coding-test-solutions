"""
개발자 장고 | 코딩테스트 알고리즘 - 1. BFS
https://www.youtube.com/watch?v=ansd5B27uJM

data structure:
    graph, queue

백준 1926번 그림
https://www.acmicpc.net/problem/1926

1. idea:
    2중 for -> 값1 & 방문X -> BFS
2. time complexity:
    BFS: O(V+E)
    V: 500 * 5--
    E: 4 * 500 * 500
    V+E = 5 * 250000
3. data structure:
    그래프 전체 지보 : int[][]
    방문: bool[][]
    queue(BFS)
"""
import sys
from collections import deque

# input = sys.stdin.readline

N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def bfs(sy: int, sx: int) -> int:
    q = deque([(sy, sx)])
    chk[sy][sx] = True
    area = 1
    
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and P[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                area += 1
                q.append((ny, nx))
    return area
    
cnt = 0
max_area = 0
for i in range(N):
    for j in range(M):
        if P[i][j] == 1 and not chk[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i, j))
            
print(cnt)
print(max_area)
