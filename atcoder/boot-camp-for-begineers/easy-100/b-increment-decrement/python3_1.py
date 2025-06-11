"""
B- Increment Decrement
https://atcoder.jp/contests/abc052/tasks/abc052_b
"""
import sys

def main() -> None:
    n = int(input().strip())
    s = str(input().strip())
    
    x = 0
    best = 0
    for c in s:
        x += 1 if c == 'I' else -1
        if x > best:
            best = x
    
    print(best)
    
if __name__ == "__main__":
    main()
