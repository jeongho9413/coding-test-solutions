"""
B- Postal Code
https://atcoder.jp/contests/abc084/tasks/abc084_b
"""
import sys

def main() -> None:
    a, b = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    
    print("Yes" if len(s) == a + b + 1 and s[a] == '-' \
        and s[:a].isdigit() and s[a + 1:].isdigit() else "No")
    
if __name__ == "__main__":
    main()
