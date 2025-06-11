"""
B - Coins
https://atcoder.jp/contests/abc087/tasks/abc087_b
"""
import sys

def main() -> None:
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    
    cnt = 0
    for i in range(a + 1):
        for j in range(b + 1):
            rest = x - 500 * i - 100 * j
            if rest < 0:
                continue
            if rest % 50 == 0:
                k = rest // 50
                if k <= c:
                    cnt += 1 
                    
    print(cnt)
    
if __name__ == "__main__":
    main()
