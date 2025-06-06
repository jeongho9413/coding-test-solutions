"""
C - Colorful Leaderboard
https://atcoder.jp/contests/abc064/tasks/abc064_c

data structure:
    string
algorithm:
    -
time complexity:
    O(N)
space complexity:
    O(1)
""" 
import sys

def main() -> None:
    # input = sys.stdin.readline
    
    N = int(input())
    ratings = list(map(int, input().split()))
    
    used = [False] * 8    # 8개의 고정 색 구간
    free = 0              # 3200 이상 (자유색) 인원 수
    
    for r in ratings:
        idx = r // 400
        if idx >= 8:
            free += 1
        else:
            used[idx] = True
            
    base = sum(used)                # 고정 구간 중 실제로 사용된 색 개수 
    min_color = max(base, 1)        # 아무도 색을 차지하지 않았으면 free 중 1명이 최소 1씩 선택
    max_color = min(base + free, 8) # free 인원이 전부 다른 색 골라도 8색 한도
    
    print(min_color, max_color)
    
if __name__ == "__main__":
    main()
