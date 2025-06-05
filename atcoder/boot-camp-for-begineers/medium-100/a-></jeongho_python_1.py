"""
A - ><
https://atcoder.jp/contests/agc040/tasks/agc040_a

data_structures:
    list
algorithms:
    Greedy, DP
time_complexity:
    O(N)
space_complexity:
    O(N)
"""
import sys

def main() -> None:
    S = sys.stdin.readline().strip()
    N = len(S)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    
    # left -> right
    for i in range(1, N + 1):
        if S[i - 1] == '<':
            L[i] = L[i - 1] + 1
            
    # right -> left
    for i in range(N - 1, -1, -1):
        if S[i] >= '>':
            R[i] = R[i + 1] + 1
            
    ans = sum(max(L[i], R[i]) for i in range(N + 1))
    print(ans)
    
if __name__ == "__main__":
    main()
