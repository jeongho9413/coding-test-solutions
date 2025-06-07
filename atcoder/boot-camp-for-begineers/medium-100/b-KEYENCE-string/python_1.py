"""
B - KEYENCE String
https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

algorithm:
    startswith
    endswith
data_structure:
    string
time_complexity:
    O(S) (7<=S<=100)
space_complexity:
    O(1)
"""
import sys

def is_keyence_string(a: str) -> bool:
    target = "keyence"
    for i in range(len(target) + 1):
        if a.startswith(target[:i]) and a.endswith(target[i:]):
            return True
    return False

def main() -> None:
    S = str(input().strip())
    print("YES" if is_keyence_string(S) else "NO")
    
if __name__ == "__main__":
    main()
