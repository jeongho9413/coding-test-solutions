import sys
from collections import deque

def main() -> None:
    n, l = map(int, sys.stdin.readline().split())
    enemies = deque()
    for i in range(n):
        enemies.append(int(sys.stdin.readline()))
        
    for i in range(n):
        enemy = enemies.popleft()
        
        if l > enemy:
            l += int(enemy // 2)
        elif l < enemy:
            l = int(l // 2)
        
    print(str(l))
        

if __name__ == "__main__":
    main()
