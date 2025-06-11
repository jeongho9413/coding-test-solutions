"""
C - Minimization
https://atcoder.jp/contests/abc101/tasks/arc099_a
"""
import sys
import math

def main() -> None:
    n, k = map(int, input().split())
    _ = sys.stdin.readline()
    
    if n <= k:
        print(1)
        return

    ans = 1 + math.ceil((n - k) / (k - 1))
    print(ans)
    
if __name__ == "__main__":
    main()
