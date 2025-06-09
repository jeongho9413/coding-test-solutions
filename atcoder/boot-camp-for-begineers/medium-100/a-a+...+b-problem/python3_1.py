"""
A - A+...+B Problem
https://atcoder.jp/contests/agc015/tasks/agc015_a

idea(algorithm):
    -
time complexity:
    -
memory complexity:
    -
data structure:
    -
"""
import sys

def main() -> None:
    N, A, B = map(int, input().split())
    
    if A > B:
        print(0)
        return
    if N == 1:
        print(1 if A == B else 0)
        return
    
    min_sum = (N - 1) * A + B
    max_sum = A + (N - 1) * B

    print(max_sum - min_sum + 1)
    
if __name__ == "__main__":
    main()
