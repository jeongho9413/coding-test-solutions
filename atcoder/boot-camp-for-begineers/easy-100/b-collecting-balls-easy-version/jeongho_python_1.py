"""
B - Collecting Balls (Easy Version)
https://atcoder.jp/contests/abc074/tasks/abc074_b

data structure:
    -
algorithm:
    -
time complexity:
    O(N)
space complexity:
    O(1)
""" 
# import sys
# import math

def main() -> None:
    # input = sys.stdin.readline
    
    N = int(input())
    K = int(input())
    xs = list(map(int, input().split()))
    
    total = sum(2 * min(x, K- x) for x in xs)
    print(total)
    
if __name__ == "__main__":
    main()
