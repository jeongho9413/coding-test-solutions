"""
C - Not so Diverse
https://atcoder.jp/contests/abc081/tasks/arc086_a

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
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    freq = Counter(A)
    kinds = len(freq)
    
    if kinds <= K:
        print(0)
        return
    
    remove_needed = kinds - K
    # deletions = sum(cnt for cnt, _ in zip(sorted(freq.values()), range(remove_needed)))
    cnts = sorted(freq.values())
    delections = sum(cnts[:remove_needed])
    print(delections)
    
if __name__ == "__main__":
    main()
