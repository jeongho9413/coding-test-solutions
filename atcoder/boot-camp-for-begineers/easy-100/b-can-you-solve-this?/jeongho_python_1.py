"""
B - Can you solve this?
https://atcoder.jp/contests/abc121/tasks/abc121_b

data_structures:
    list
algorithms:
    linear scan, dot product
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    
    cnt = 0
    for _ in range(n):
        A = list(map(int, input().split()))
        score = sum(a * b for a, b in zip(A, B))
        if score > 0:
            cnt += 1
            
    print(cnt)
    
if __name__ == "__main__":
    main()
