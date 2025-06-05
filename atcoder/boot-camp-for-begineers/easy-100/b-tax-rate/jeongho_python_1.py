"""
B - Tax Rate
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

algorithms:
    brute force, linear search
"""
import sys

N = int(sys.stdin.readline())
# N = int(input())

for x in range(1, 50000):
    if (x * 108) // 100 == N:
        print(x)
        break

else:
    print(":(")
