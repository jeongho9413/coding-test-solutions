"""
C - Exception Handling
https://atcoder.jp/contests/abc134/tasks/abc134_c
"""
import sys

def main() -> None:
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for _ in range(n)]
    
    max1, max2 = -1, -1
    for i in a:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
            
    out_lines = [str(max2 if i == max1 else max1) for i in a]
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == "__main__":
    main()
