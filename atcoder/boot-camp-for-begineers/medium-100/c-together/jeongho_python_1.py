"""
C - Together
https://atcoder.jp/contests/abc072/tasks/arc082_a

data structure:
    counter
algorithm:
    -
time complexity:
    O(N + U)
space complexity:
    O(U)
""" 
import sys
from collections import Counter

def main() -> None:
    n = list(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
     
    freq = Counter(a)
    best = 0
     
    for i in freq:
        s = freq[i - 1] + freq[i] + freq[i + 1]
        if s > best:
            best = s
             
    print(best)
    
if __name__ == "__main__":
    main()
