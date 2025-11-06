import sys

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    grid = list()
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().strip().split())))
        
    res = [0] * k
    for i in range(n):
        if i == 0:
            cur_min = grid[0].copy()
            continue
        
        for j in range(k):
            if cur_min[j] > grid[i][j]:
                cur_min[j] = grid[i][j]
                res[j] = i
                
    print(len(set(res)))
        

if __name__ == "__main__":
    main()
