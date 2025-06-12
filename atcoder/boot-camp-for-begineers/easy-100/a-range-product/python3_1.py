"""
A - Range Product
https://atcoder.jp/contests/agc002/tasks/agc002_a
"""
import sys

def main() -> None:
    a, b = map(int, sys.stdin.readline().split())
    
    if a <= 0 <= b:
        print("Zero")
    elif a > 0:
        print("Positive")
    else:
        print("Positive" if (b - a + 1) % 2 == 0 else "Negative")
    
if __name__ == "__main__":
    main()
