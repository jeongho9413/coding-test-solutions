"""
A - Cookie Exchanges
https://atcoder.jp/contests/agc014/tasks/agc014_a

time complexity:
    O(M), M = max(A, B, C)
space complexity:
    O(1)
"""
import sys

def main() -> None:
    A, B, C = map(int, input().split())
    
    if A == B == C and A % 2 == 0:
        print(-1)
        return

    cnt = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = (B + C) // 2, (C + A) // 2, (A + B) // 2
        cnt += 1
        
    print(cnt)
        
if __name__ == "__main__":
    main()
