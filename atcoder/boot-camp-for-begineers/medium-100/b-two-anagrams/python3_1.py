"""
B - Two Anagrams
https://atcoder.jp/contests/abc082/tasks/abc082_b
"""
import sys

def main() -> None:
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    s_sorted = ''.join(sorted(s))
    t_sorted = ''.join(sorted(t, reverse=True))
    
    print("Yes" if s_sorted < t_sorted else "No")
    
if __name__ == "__main__":
    main()
