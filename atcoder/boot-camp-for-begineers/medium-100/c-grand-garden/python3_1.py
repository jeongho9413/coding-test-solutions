"""
C - Grand Garden
https://atcoder.jp/contests/abc116/tasks/abc116_c
"""
import sys

def main() -> None:
    n = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split()))
    
    prev = 0
    ops = 0
    
    for h_temp in h:
        if h_temp > prev:
            ops += h_temp - prev
        prev = h_temp
        
    print(ops) 
    
if __name__ == "__main__":
    main()
