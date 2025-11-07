import sys

def main() -> None:
    n, k = map(int, sys.stdin.readline().strip().split())
    grid = list()
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().strip().split())))
    hs = set(list(map(int, sys.stdin.readline().strip().split())))
    hs.add(0)
    cnt = 0
    
    grid_boolean = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] in hs:
                grid_boolean[i][j] = True
                
    # rows
    for i in range(n):
        if all(grid_boolean[i]):
            cnt += 1
            
    # cols
    for j in range(n):
        temp = list()
        for i in range(n):
            temp.append(grid_boolean[i][j])
        if all(temp):
            cnt += 1
            
    # diag 1
    temp = list()
    for i in range(n):
        temp.append(grid_boolean[i][i])
    if all(temp):
        cnt += 1
            
    # diag 2
    temp = list()
    for i in range(n):
        temp.append(grid_boolean[i][n - i - 1])
    if all(temp):
        cnt += 1
            
    sys.stdout.write(f"{cnt}")


if __name__ == "__main__":
    main()
