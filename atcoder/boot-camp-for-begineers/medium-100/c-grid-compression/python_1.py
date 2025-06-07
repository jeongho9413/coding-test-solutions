"""
B - Grid Compression
https://atcoder.jp/contests/abc107/tasks/abc107_b

algorithm:
    -
data_structure:
    -
time_complexity:
    O(HW)
space_complexity:
    O(H+W)
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    H, W = map(int, input().split())
    grid = [input().rstrip() for _ in range(H)]
    
    keep_row = [any(ch == '#' for ch in row) for row in grid]
    keep_col = [any(grid[r][c] == '#' for r in range(H)) for c in range(W)]
    
    for r in range(H):
        if not keep_row[r]:
            continue
        
        line = []
        for c in range(W):
            if keep_col[c]:
                line.append(grid[r][c])
        print(''.join(line))

if __name__ == "__main__":
    main()
