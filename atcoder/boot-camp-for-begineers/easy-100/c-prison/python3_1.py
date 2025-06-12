"""
C - Prison
https://atcoder.jp/contests/abc127/tasks/abc127_c
"""
import sys
import math

def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    l_max = 1
    r_min = n
    
    for _ in range(m):
        l, r = map(int, sys.stdin.readline().split())
        l_max = max(l_max, l)
        r_min = min(r_min, r)
        
    ans = max(0, r_min - l_max + 1)
    print(ans)
    
if __name__ == "__main__":
    main()
