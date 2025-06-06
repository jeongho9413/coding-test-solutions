"""
B - Minesweeper
https://atcoder.jp/contests/abc075/tasks/abc075_b

data structure:
    -
algorithm:
    -
""" 
def main() -> None:
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)
    
    out = [[''] * W for _ in range(H)]
    
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#':
                out[h][w] = '#'
                continue

            cnt = 0
            for i in range(8):
                nh, nw = h + dx[i], w + dy[i]
                if 0 <= nh < H and 0 <= nw < W and grid[nh][nw] == '#':
                    cnt += 1
            out[h][w] = str(cnt)
            
    for row in out:
        print(''.join(row))
        
if __name__ == "__main__":
    main()
