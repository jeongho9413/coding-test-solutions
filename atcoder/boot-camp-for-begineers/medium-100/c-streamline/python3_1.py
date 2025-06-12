"""
C - Streamline
https://atcoder.jp/contests/abc117/tasks/abc117_c
"""
import sys

def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    x = sorted(map(int, sys.stdin.readline().split()))
    
    if m <= n:
        print(0)
        return
    
    gaps = sorted((x[i + 1] - x[i] for i in range(m - 1)), reverse = True)
    min_moves = sum(gaps[n - 1:])
    print(min_moves)
    
if __name__ == "__main__":
    main()
