"""
C - Go to School
https://atcoder.jp/contests/abc142/tasks/abc142_c
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    N = int(input())
    P = list(map(int, input().split()))
    
    ans = [0] * N
    for i, p in enumerate(P):
        ans[p - 1] = i + 1
    
    print(*ans)
    
if __name__ == "__main__":
    main()
