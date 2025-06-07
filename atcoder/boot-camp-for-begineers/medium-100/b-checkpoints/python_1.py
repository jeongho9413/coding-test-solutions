"""
B - Checkpoints
https://atcoder.jp/contests/abc057/tasks/abc057_b

algorithm:
    -
data_structure:
    -
time_complexity:
    -
space_complexity:
    O(N+M)
"""
import sys

def main() -> None:
    input = sys.stdin.readline

    N, M = map(int, input().split())
    student_arr = [tuple(map(int, input().split())) for _ in range(N)]
    check_arr   = [tuple(map(int, input().split())) for _ in range(M)]
    
    for sx, sy in student_arr:
        idx_best = -1
        dist_best = 1e18
        
        for j, (cx, cy) in enumerate(check_arr, start=1):
            dist = abs(sx - cx) + abs(sy - cy)
            if dist < dist_best:
                dist_best = dist
                idx_best = j

        print(idx_best)
        
if __name__ == "__main__":
    main()
