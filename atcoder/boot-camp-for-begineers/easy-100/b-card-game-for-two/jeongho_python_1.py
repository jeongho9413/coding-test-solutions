"""
B - Card Game for Two
https://atcoder.jp/contests/abc088/tasks/abc088_b

data structure:
    list
algorithm:
    optimization
    list.sort
""" 
# import sys
# import math

def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort(reverse=True)
    
    alice = sum(A[0::2])
    bob = sum(A[1::2])
    
    print(alice - bob)
    
if __name__ == "__main__":
    main()
