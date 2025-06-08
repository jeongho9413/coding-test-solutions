"""
C - Bugged
https://atcoder.jp/contests/abc063/tasks/arc075_a

idea(algorithm):
    -
time complexity:
    -
memory complexity:
    O(N)
data structure:
    O(1)
"""
import sys

def main() -> None:
    N = int(input().strip())
    S = [int(input()) for _ in range(N)]
    
    total = sum(S)
    if total % 10 != 0:
        print(total)
        return
    
    min_S = min((x for x in S if x % 10 != 0), default=None)
    
    if min_S is None:
        print(0)
    else:
        print(total - min_S)
        
if __name__ == "__main__":
    main()
