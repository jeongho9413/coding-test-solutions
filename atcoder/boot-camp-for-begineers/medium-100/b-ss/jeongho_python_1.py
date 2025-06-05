"""
B - ss
https://atcoder.jp/contests/abc066/tasks/abc066_b

data_structures:
    string
algorithms:
    -
time_complexity:
    -
space_complexity:
    -
"""
import sys

def main() -> None:
    S = sys.stdin.readline().strip()
    n = len(S)
    
    for l in range(n - 2, 0, -2):
        half = l // 2
        if S[:half] == S[half:l]:
            print(l)
            return
        
if __name__ == "__main__":
    main()
