"""
D - Banned K
https://atcoder.jp/contests/abc159/tasks/abc159_d

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
from collections import Counter

def main() -> None:
    n = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    
    freq = Counter(A)
    total_pairs = sum(c * (c -1) // 2 for c in freq.values())
    
    for x in A:
        c = freq[x]
        print(total_pairs - (c - 1))
        
if __name__ == "__main__":
    main()
