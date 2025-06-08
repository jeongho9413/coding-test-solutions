"""
C - Write and Erase
https://atcoder.jp/contests/abc073/tasks/abc073_c

idea(algorithm):
    -
time complexity:
    -
memory complexity:
    O(N)
data structure:
    최악 -> O(N) < 2e5
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    N = int(input())
    S = set()
    
    for _ in range(N):
        x = int(input())
        if x in S:
            S.remove(x)
        else:
            S.add(x)
            
    print(len(S))
    
if __name__ == "__main__":
    main()
