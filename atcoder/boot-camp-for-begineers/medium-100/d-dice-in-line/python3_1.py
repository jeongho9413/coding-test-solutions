"""
D - Dice in Line
https://atcoder.jp/contests/abc154/tasks/abc154_d

아이디어:
    등차수열
    누적합
"""
import sys

def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    
    e = [(i + 1) / 2 for i in p]
    
    prefix = [0.]
    for j in e:
        prefix.append(prefix[-1] + j)
        
    best = 0.
    for i in range(k, n + 1):
        cur = prefix[i] - prefix[i - k]
        best = max(best, cur)
        
    print(f"{best:.10f}") 
    
if __name__ == "__main__":
    main()
