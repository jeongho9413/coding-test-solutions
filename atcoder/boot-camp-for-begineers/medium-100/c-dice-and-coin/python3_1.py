"""
C - Dice and Coin
https://atcoder.jp/contests/abc126/tasks/abc126_c

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
import math

def main() -> None:
    N, K = map(int, sys.stdin.readline().split())
    
    prob = 0.0
    for i in range(1, N + 1):
        need = 0 
        x = i
        while x < K:
            x *= 2
            need += 1
              
        prob += math.pow(0.5, need)
        
    print(prob / N)
    
if __name__ == "__main__":
    main()
