"""
A - Prefix and Suffix
https://atcoder.jp/contests/agc006/tasks/agc006_a
"""
import sys

def main() -> None:
    _ = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    n = len(s)
    
    max_overlap = 0
    for i in range(n, -1, -1):
        if s[n - i:] == t[:i]:
            max_overlap = i
            break
        
    print(2 * n - max_overlap)
    
if __name__ == "__main__":
    main()
