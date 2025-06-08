"""
B - Toll Gates
https://atcoder.jp/contests/abc094/tasks/abc094_b

idea:
    -
time complexity:
    -
memory complexity:
    -
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    left = sum(1 for a in A if a < X)
    right = M - left
    
    print(min(left, right))
    
if __name__ == "__main__":
    main()
