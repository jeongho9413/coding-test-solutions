"""
C - Otoshidama
https://atcoder.jp/contests/abc085/tasks/abc085_c
"""
import sys

def main() -> None:
    n, y = map(int, input().split())
    
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            if 10000 * i + 5000 * j + 1000 * k == y:
                print(i, j, k)
                return
            
    print(-1, -1, -1)
    
if __name__ == "__main__":
    main()
