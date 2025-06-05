"""
B - Qualification_simulator
https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b

algorithms:
    greedy, counter
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    n, a, b = list(map(int, input().split()))
    s = input().strip()
    
    total_p = 0
    oversea_p = 0
    
    out_lines = list()
    for ch in s:
        if ch == 'a':
            if total_p < a + b:
                out_lines.append("Yes")
                total_p += 1
            else:
                out_lines.append("No")
                
        elif ch == 'b':
            if total_p < a + b and oversea_p < b:
                out_lines.append("Yes")
                total_p += 1
                oversea_p += 1
            else:
                out_lines.append("No")
        
        else:
            out_lines.append("No")
            
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == "__main__":
    main()
