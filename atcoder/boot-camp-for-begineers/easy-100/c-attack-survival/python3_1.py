"""
C - Attack Survival
https://atcoder.jp/contests/abc141/tasks/abc141_c
"""
import sys

def main() -> None:
    n, k, q = map(int, sys.stdin.readline().split())
    cnt = [0] * n
    
    for _ in range(q):
        a = int(sys.stdin.readline())
        cnt[a - 1] += 1
        
    for c in cnt:
        print("Yes" if k - q + c > 0 else "No")
    
if __name__ == "__main__":
    main()
