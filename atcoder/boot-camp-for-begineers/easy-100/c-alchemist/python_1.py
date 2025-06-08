"""
C - Alchemist
https://atcoder.jp/contests/abc138/tasks/abc138_c

idea:
    오름차순으로 합성해가기 -> 오름차순 정렬
    가중 평균 전개
time complexity:
    O(NlogN)
memory complexity:
    O(1)
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    N = int(input())
    V = sorted(map(float, input().split()))
    
    cur = V[0]
    for i in range(1, N):
        cur = (cur + V[i]) / 2
        
    print(cur)
    
if __name__ == "__main__":
    main()
