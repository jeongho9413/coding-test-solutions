"""
C - Divide the Problems
https://atcoder.jp/contests/abc132/tasks/abc132_c

algorithm:
    sorting
data_structure:
    array
time_complexity:
    O(NlogN)
space_complexity:
    O(1)
"""
import sys

def main() -> None:
    N = int(input())
    D_arr = list(map(int, input().split()))
    
    D_arr.sort()
    mid = N // 2
    ans = D_arr[mid] - D_arr[mid - 1]
    print(ans)
    
if __name__ == "__main__":
    main()
