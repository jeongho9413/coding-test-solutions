"""
C - 4-adjacent
https://atcoder.jp/contests/abc069/tasks/arc080_a
"""
import sys

def main() -> None:
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    
    c4 = sum(x % 4 == 0 for x in a)
    c2 = sum(x % 2 == 0 and x % 4 != 0 for x in a)
    c1 = len(a) - c4 - c2

    print("Yes" if c4 >= c1 or (c4 == c1 - 1 and c2 == 0) else "No")
    
if __name__ == "__main__":
    main()
