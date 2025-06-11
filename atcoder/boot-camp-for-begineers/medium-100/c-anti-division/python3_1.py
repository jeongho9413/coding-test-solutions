"""
C - Minimization
https://atcoder.jp/contests/abc101/tasks/arc099_a
"""
import sys
import math

def solution(n: int, c: int, d: int) -> int:
    lcm = c // math.gcd(c, d) * d
    return n - n // c - n // d + n // lcm

def main() -> None:
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    ans = solution(b, c, d) - solution(a - 1, c, d)
    print(ans)
    return
    
if __name__ == "__main__":
    main()
