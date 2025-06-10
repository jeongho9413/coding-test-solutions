"""
A - Sorted Arrays
https://atcoder.jp/contests/agc013/tasks/agc013_a
"""
import sys

def main() -> None:
    _ = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    ans = 1
    trend = 0
    
    for i in range(1, len(a)):
        diff = a[i] - a[i  -1]
        
        if diff == 0:
            continue
        
        sign = 1 if diff > 0 else -1
        
        if trend == 0:
            trend = sign
        elif trend != sign:
            ans += 1
            trend = 0
            
    print(ans)
    
if __name__ == "__main__":
    main()
