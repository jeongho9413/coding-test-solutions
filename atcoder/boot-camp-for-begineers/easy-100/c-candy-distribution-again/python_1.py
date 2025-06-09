"""
A - Candy Distribution Again
https://atcoder.jp/contests/agc027/tasks/agc027_a

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
    n, x = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    
    satisfied = 0
    for i in arr:
        if x >= i:
            x -= i
            satisfied += 1
        else:
            break
        
    if satisfied == n and x > 0:
        satisfied -= 1
        
    print(satisfied)
    
if __name__ == "__main__":
    main()
