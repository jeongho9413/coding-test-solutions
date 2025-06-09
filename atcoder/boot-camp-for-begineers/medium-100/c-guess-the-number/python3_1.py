"""
C - Guess The Number
https://atcoder.jp/contests/abc157/tasks/abc157_c

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
    N, M = map(int, input().split())
    
    digit = [-1] * N
    ok = True
    
    for _ in range(M):
        s, c = map(int, sys.stdin.readline().split())
        idx = s - 1
        if digit[idx] != -1 and digit[idx] != c:
            ok = False
        digit[idx] = c

    if N > 1:
        if digit[0] == 0:
            ok = False
        elif digit[0] == -1:
            digit[0] = 1
    else:
        if digit[0] == -1:
            digit[0] == 0
            
    if not ok:
        print(-1)
        return
    
    for i in range(N):
        if digit[i] == -1:
            digit[i] = 0
            
    print(''.join(map(str, digit)))
    
if __name__ == "__main__":
    main()
