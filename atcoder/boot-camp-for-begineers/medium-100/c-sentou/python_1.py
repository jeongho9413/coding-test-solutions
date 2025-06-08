"""
C - Sentou
https://atcoder.jp/contests/abc060/tasks/arc073_a

idea(algorithm):
    -
time complexity:
    -
memory complexity:
    O(N)
data structure:
    -
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    N, T = map(int, input().split())
    times = list(map(int, input().split()))
    
    total = T
    for i in range(N - 1):
        gap = times[i + 1] - times[i]
        total += min(T, gap)
        
    print(total)
    
if __name__ == "__main__":
    main()
