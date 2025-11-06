import sys

def main() -> None:
    n = int(sys.stdin.readline())
    grid = list()
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))
        
    res = 0
    for i in range(n):
        for j in range(n):
            val = 1 + min(i, j, n - i - 1, n - j - 1)
            res += max(0, (grid[i][j] - val))
    print(res)

if __name__ == "__main__":
    main()
