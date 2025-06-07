"""
C - Grid Repainting 2
https://atcoder.jp/contests/abc096/tasks/abc096_c

algorithm:
    Brute_force
data_structure:
    array
time_complexity:
    O(HW)
space_complexity:
    O(HW)
"""
import sys

def main() -> None:
    input = sys.stdin.readline
    
    H, W = map(int, input().split())
    G = [input().strip() for _ in range(H)]
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
    for r in range(H):
        for c in range(W):
            if G[r][c] == '#':
                ok = False
                for k in range(4):
                    nr, nc = r + dx[k], c + dy[k]
                    if 0 <= nr < H and 0 <= nc < W and G[nr][nc] == '#':
                        ok = True
                        break
                if not ok:
                    print("No")
                    return
                
    print("Yes")
    
if __name__ == "__main__":
    main()
