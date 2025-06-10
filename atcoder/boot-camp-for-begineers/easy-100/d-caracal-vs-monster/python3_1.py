"""
D - Caracal vs Monster
https://atcoder.jp/contests/abc153/tasks/abc153_d

아이디어:
    분할 트리
"""
import sys

class Solution:
    @staticmethod
    def attacks(h: int) -> int:
        if h == 1:
            return 1
        half = h // 2
        return 1 + 2 * Solution.attacks(half)
    
def main() -> None:
    h = int(sys.stdin.readline())
    print(Solution.attacks(h))
    
if __name__ == "__main__":
    main()
