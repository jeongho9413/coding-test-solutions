"""
C - Flip,Flip, and Flip
https://atcoder.jp/contests/abc090/tasks/arc091_a
"""
import sys

def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    
    if n == 1 and m == 1:
        ans = 1
    elif n == 1:
        ans = max(0, m - 2)
    elif m == 1:
        ans = max(0, n - 2)
    elif n == 2 or m == 2:
        ans = 0
    else:
        ans = (n - 2) * (m - 2)
        
    print(ans)
    
if __name__ == "__main__":
    main()
