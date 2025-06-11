"""
B - Varied
https://atcoder.jp/contests/abc063/tasks/abc063_b
"""
import sys

def main() -> None:
    s = str(sys.stdin.readline().strip())
    print("yes" if len(set(s)) == len(s) else "no")
    
if __name__ == "__main__":
    main()
