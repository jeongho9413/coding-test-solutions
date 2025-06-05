"""
D - ModSum
https://atcoder.jp/contests/abc139/tasks/abc139_d

data_structures:
    INT
algorithms:
    Upper Bound: N(N - 1)/2
time_complexity:
    O(1)
space_complexity:
    O(1)
"""
import sys

def main() -> None:
    N = int(sys.stdin.readline())
    result = N * (N - 1) // 2
    print(result)
    
if __name__ == "__main__":
    main()
