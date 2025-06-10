"""
B - Shift only
https://atcoder.jp/contests/abc081/tasks/abc081_b
"""
import sys

class Solution:
    @staticmethod
    def cnt_trailing_zeros(x: int) -> int:
        cnt = 0
        while x % 2 == 0:
            x //= 2
            cnt += 1
        return cnt
    
def main() -> None:
    _ = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    ans = min(Solution.cnt_trailing_zeros(x) for x in a)
    print(ans)
    
if __name__ == "__main__":
    main()
