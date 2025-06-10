"""
B - 754
https://atcoder.jp/contests/abc114/tasks/abc114_b
"""
import sys

class Solution:
    @staticmethod
    def jeongho(s: str) -> int:
        target = 753
        best = float('inf')
        
        for i in range(len(s) - 2):
            num = int(s[i:i + 3])
            diff = abs(target - num)
            best = min(best, diff)
            
        return best
    
def main() -> None:
    s = str(sys.stdin.readline())
    print(Solution.jeongho(s))
    
if __name__ == "__main__":
    main()
