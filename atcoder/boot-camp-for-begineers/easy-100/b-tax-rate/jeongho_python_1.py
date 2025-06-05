"""
B - Tax Rate
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

algorithms:
    brute force, linear search
"""
import sys

def solution(n: int) -> None:
    for x in range(1, 50000):
        if (x * 108) // 100 == n:
            print(x)
            break
        else:
            print(":(")
            
n = int(sys.stdin.readline())
solution(n)
