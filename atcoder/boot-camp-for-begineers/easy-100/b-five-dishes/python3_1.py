"""
B - Five Dishes
https://atcoder.jp/contests/abc123/tasks/abc123_b
"""
import sys
import math

def main() -> None:
    times = [int(sys.stdin.readline()) for _ in range(5)]
    
    gaps = [(((t + 9) // 10) * 10 - t) for t in times]
    
    idx_last = gaps.index(max(gaps))
    
    total = 0
    for i, t in enumerate(times):
        if i == idx_last:
            total += t
        else:
            total += math.ceil(t / 10) * 10
            
    print(total)
    
if __name__ == "__main__":
    main()
