"""
B - Count Balls
https://atcoder.jp/contests/abc158/tasks/abc158_b
"""
import sys

class Solution:
    @staticmethod
    def cycle(n: int, a: int, b: int) -> int:
        cycles = n // (a + b)
        rem = n % (a + b)
        
        return cycles * a + min(a, rem)
    
def main() -> None:
    n, a, b = map(int, sys.stdin.readline().split())
    print(Solution.cycle(n, a, b))
    
if __name__ == "__main__":
    main()
