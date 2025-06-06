"""
B - Choose Integers
https://atcoder.jp/contests/abc060/tasks/abc060_b

data structure:
    -
algorithm:
    -
time complexity:
    O(B)
space complexity:
    O(1)
""" 
import sys

def main() -> None:
    A, B, C = map(int, input().split())
    
    rem = 0
    for _ in range(1, B + 1):
        rem = (rem + A) % B
        if rem == C:
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    main()
