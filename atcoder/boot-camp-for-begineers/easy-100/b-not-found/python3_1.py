"""
B - Not Found
https://atcoder.jp/contests/abc071/tasks/abc071_b
"""
import sys

def main() -> None:
    s = sys.stdin.readline().strip()
    used = set(s)
    for c in map(chr, range(ord('a'), ord('z') + 1)):
        if c not in used:
            print(c)
            return
        
    print('None')
    
if __name__ == "__main__":
    main()
