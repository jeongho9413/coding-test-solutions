"""
B - Trained?
https://atcoder.jp/contests/abc065/tasks/abc065_b
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    n = int(input())
    nxt = [0] + [int(input()) for _ in range(n)]
    
    cur = 1
    step = 0
    visited = [False] * (n + 1)
    
    while True:
        if cur == 2:
            print(step)
            return
        if visited[cur]:
            print(-1)
            return
        visited[cur] = True
        cur = nxt[cur]
        step += 1
        
if __name__ == "__main__":
    main()
