"""
A - Irreversible operation
https://atcoder.jp/contests/agc029/tasks/agc029_a

data_structures:
    -
algorithms:
    -
time_complexity:
    O(N)
space_complexity:
    O(1)
"""
import sys

def main() -> None:
    s = sys.stdin.readline().strip()
    
    cnt_B = 0
    ans = 0
    
    for ch in s:
        if ch == 'B':
            cnt_B += 1
        else:
            ans += cnt_B
            
    print(ans)
    
if __name__ == "__main__":
    main()
