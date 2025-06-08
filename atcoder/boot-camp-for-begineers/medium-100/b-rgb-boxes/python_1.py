"""
B - RGB Boxes
https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b

idea(algorithm):
    -
time complexity:
    -
memory complexity:
    -
data structure:
    -
"""
import sys

def main() -> None:
    R, G, B, N = map(int, sys.stdin.readline().split())
    
    ans = 0
    for r in range(0, N // R + 1):
        rem_after_r = N - r * R
        for g in range(0, rem_after_r // G + 1):
            rem = rem_after_r - g * G
            if rem % B == 0:
                ans += 1
                
    print(ans)
    
if __name__ == "__main__":
    main()
