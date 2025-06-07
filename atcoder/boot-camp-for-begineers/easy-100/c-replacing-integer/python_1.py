"""
C - Replacing Integer
https://atcoder.jp/contests/abc161/tasks/abc161_c

algorithm:
    min(a, K-a)
data_structure:
    -
time_complexity:
    O(1)
space_complexity:
    O(1)
"""
import sys

def main() -> None:
    N, K = map(int, input().split())
    
    if K == 0:
        print(N)
        return
    
    else:
        a = N % K
        ans = min(a, K - a)
        print(ans)
        
if __name__ == "__main__":
    main()
