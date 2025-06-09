"""
C - Count Order
https://atcoder.jp/contests/abc150/tasks/abc150_c

idea(algorithm):
    -
time complexity:
    O(N^2), N <= 8
memory complexity:
    -
data structure:
    -
"""
import sys
import math

def rank_of_perm(perm: list[int]) -> int:
    n = len(perm)
    used = [False] * (n + 1)
    rank = 0
    for i, v, in enumerate(perm):
        c = sum(1 for x in range(1, v) if not used[x])
        rank += c * math.factorial(n - 1 - i)
        used[v] = True
    return rank

def main() -> None:
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    
    rp = rank_of_perm(P)
    rq = rank_of_perm(Q)
    print(abs(rp - rq))
    
if __name__ == "__main__":
    main()
