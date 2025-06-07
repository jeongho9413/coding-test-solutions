"""
B - Break Number
https://atcoder.jp/contests/abc068/tasks/abc068_b

time complexity:
    O(1)
"""
def main() -> None:
    N = int(input().strip())
    
    p = 1
    while (p * 2) <= N:   # while (p << 1) <= N
        p *= 2            # p <<= 1
    print(p)
    
if __name__ == "__main__":
    main()
