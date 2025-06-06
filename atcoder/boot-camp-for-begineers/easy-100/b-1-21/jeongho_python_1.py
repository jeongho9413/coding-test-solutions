"""
B - 1 21
https://atcoder.jp/contests/abc086/tasks/abc086_b

data structure:
    -
algorithm:
    math.isqrt
""" 
import sys
import math

def main() -> None:
    a, b = map(int, input().split())

    ab = int(f"{a}{b}")

    r = math.isqrt(ab)
    ok = (r * r == ab)

    print("Yes" if ok else "No")

if __name__ == "__main__":
    main()
