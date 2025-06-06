"""
B - Bishop 
https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b

data structure:
    -
algorithm:
    -
""" 
def main() -> None:
    H, W = map(int, input().split())
    
    if H == 1 or W == 1:
        print(1)
        return
    
    print((H * W + 1) // 2)
    
if __name__ == "__main__":
    main()
