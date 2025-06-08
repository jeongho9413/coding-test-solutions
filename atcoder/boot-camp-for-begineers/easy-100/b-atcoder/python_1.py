"""
B - ATCoder
https://atcoder.jp/contests/abc122/tasks/abc122_b

idea:
    -
time complexity:
    O(N)
memory complexity:
    O(1)
"""
import sys

def main() -> None:
    S = str(input().strip())
    good = {'A', 'C', 'G', 'T'}
    
    cur = best = 0
    for ch in S:
        if ch in good:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
            
    print(best)
    
if __name__ == "__main__":
    main()
