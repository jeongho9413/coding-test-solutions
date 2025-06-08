"""
C - Takahashi's Information
https://atcoder.jp/contests/abc088/tasks/abc088_c

idea(algorithm):
    -
time complexity:
    O(1)
memory complexity:
    O(1)
data structure:
    2D-array
"""
import sys

def main() -> None:
    c = [list(map(int, input().split())) for _ in range(3)]
    
    b = c[0][:]
    
    for i in range(3):
        ai = c[i][0] - b[0]
        for j in range(3):
            if c[i][j] != ai + b[j]:
                print("No")
                return
    
    print("Yes")
    
if __name__ == "__main__":
    main()
