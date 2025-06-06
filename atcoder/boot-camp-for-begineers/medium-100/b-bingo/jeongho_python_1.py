"""
B - Bingo
https://atcoder.jp/contests/abc157/tasks/abc157_b

data structure:
    set, list/dict
algorithm:
    완전 탐색
"""
import sys

def main() -> None:
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    called = {int(input()) for _ in range(N)}
    
    mark = [[A[r][c] in called for c in range(3)] for r in range(3)]
    bingo = False
    
    for r in range(3):
        if all(mark[r]):
            bingo = True
            break
        
    if not bingo:
        for c in range(3):
            if all(mark[r][c] for r in range(3)):
                bingo = True
                break
            
    if not bingo:
        if all(mark[i][i] for i in range(3)) or all(mark[i][2 - i] for i in range(3)):
            bingo = True
            
    print("Yes" if bingo else "No")
    
if __name__ == "__main__":
    main()
