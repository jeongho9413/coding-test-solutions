"""
B - Nice Shopping
https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_b

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
    A, B, M = map(int, sys.stdin.readline().split())
    frige = list(map(int, sys.stdin.readline().split()))
    micro = list(map(int, sys.stdin.readline().split()))
    
    best = min(frige) + min(micro)
    
    for _ in range(M):
        x, y, c = map(int, sys.stdin.readline().split())
        cost = frige[x - 1] + micro[y - 1] - c
        if cost < best:
            best = cost
            
    print(best)
    
if __name__ == "__main__":
    main()
