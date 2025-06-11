"""
B - Unhappy Hacking (ABC Edit)
https://atcoder.jp/contests/abc043/tasks/abc043_b
"""
import sys

def main() -> None:
    s = input().strip()
    
    out = list()
    for c in s:
        if c == 'B':
            if out:
                out.pop()
        else:
            out.append(c)
    print(''.join(out))
    
if __name__ == "__main__":
    main()
