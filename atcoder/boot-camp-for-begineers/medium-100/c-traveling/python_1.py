"""
C - Traveling
https://atcoder.jp/contests/abc086/tasks/arc089_a

algorithm:
    Manhattan_distance, Parity_check
data_structure:
    INT
time_complexity:
    O(N)
space_complexity:
    O(1)
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    N = int(input())
    prev_t, prev_x, prev_y = 0, 0, 0
    
    for _ in range(N):
        t, x, y = map(int, input().split())
        dt = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)
        
        if dist > dt or (dist & 1) != (dt & 1):
            print("No")
            return
        
        prev_t, prev_x, prev_y = t, x, y
        
    print("Yes")
    
if __name__ == "__main__":
    main()
