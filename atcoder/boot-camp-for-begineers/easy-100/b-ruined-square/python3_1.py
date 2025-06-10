"""
B - Ruined Square
https://atcoder.jp/contests/abc108/tasks/abc108_b
"""
import sys
from typing import List

class Solution:
    @staticmethod
    def jeongho(x1: int, y1: int, x2: int, y2: int) -> List[int]:
        dx = x2 - x1
        dy = y2 - y1

        x3 = x2 - dy
        y3 = y2 + dx

        x4 = x3 - dx
        y4 = y3 - dy
        
        return x3, y3, x4, y4
    
def main() -> None:
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    arr = Solution.jeongho(x1, y1, x2, y2)
    print(*arr)
    
if __name__ == "__main__":
    main()
