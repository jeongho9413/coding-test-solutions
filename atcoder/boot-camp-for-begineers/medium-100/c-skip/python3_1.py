"""
C - Skip
https://atcoder.jp/contests/abc109/tasks/abc109_c
"""
import sys
import math
import functools

def main() -> None:
    n, x = map(int, sys.stdin.readline().split())
    cities = list(map(int, sys.stdin.readline().split()))
    
    diffs = [abs(c - x) for c in cities]
    
    ans = functools.reduce(math.gcd, diffs)
    print(ans)
    
if __name__ == "__main__":
    main()
