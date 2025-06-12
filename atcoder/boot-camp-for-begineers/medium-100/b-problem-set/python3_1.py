"""
B - Problem Set
https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b
"""
import sys
from collections import Counter

def main() -> None:
    n = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    
    stock = Counter(d)
    for t_temp in t:
        if stock[t_temp] == 0:
            print("NO")
            return
        stock[t_temp] -= 1
        
    print("YES")
    
if __name__ == "__main__":
    main()
