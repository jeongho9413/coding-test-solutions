"""
C - Traveling Salesman around Lake
https://atcoder.jp/contests/abc160/tasks/abc160_c

time complexity:
    O(N)
"""
import sys

def main() -> None:
    K, N = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    max_gap = 0
    for i in range(1, N):
        max_gap = max(max_gap, A[i] - A[i - 1])
    max_gap = max(max_gap, K - A[-1] + A[0])

    print(K - max_gap)

if __name__ == "__main__":
    main()
