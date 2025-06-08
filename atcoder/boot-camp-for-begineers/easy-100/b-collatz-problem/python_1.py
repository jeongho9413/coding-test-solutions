"""
B - Collatz Problem
https://atcoder.jp/contests/abc116/tasks/abc116_b

idea(algorithm):
    -
time complexity:
    O(L)
memory complexity:
    O(L)
data structure:
    set
"""
import sys

def main() -> None:
    s = int(input().strip())
    
    seen = {s}
    cur = s
    idx = 1
    
    while True:
        idx += 1
        cur = cur // 2 if cur % 2 == 0 else 3 * cur + 1
        
        if cur in seen:
            print(idx)
            return
        seen.add(cur)
        
if __name__ == "__main__":
    main()
