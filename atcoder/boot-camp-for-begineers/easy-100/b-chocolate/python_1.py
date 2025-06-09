"""
B - Chocolate
https://atcoder.jp/contests/abc092/tasks/abc092_b

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
    N = int(input())
    D, X = map(int, input().split())
    
    total = X
    for _ in range(N):
        A = int(input())
        total += (D - 1) // A + 1
        
    print(total)
    
if __name__ == "__main__":
    main()
