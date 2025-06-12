"""
C - When I hit my pocket
https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_c
"""
import sys

def main() -> None:
    k, a, b = map(int, sys.stdin.readline().split())
    
    if b - a <= 2:
        print(1 + k)
        return
    if k < a:
        print(1 + k)
        return
    
    biscuits = a
    k -= (a - 1)
    gain_per_cycle = b - a
    biscuits += (k // 2) * gain_per_cycle
    biscuits += k % 2
    
    print(biscuits)
    
if __name__ == "__main__":
    main()
