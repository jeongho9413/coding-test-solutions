from typing import List

"""using while func"""
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
        
    return -1

def main() -> None:
    arr = list(map(int, input().split()))
    target = int(input().strip())
    
    print(binary_search(arr, target))
    
if __name__ == "__main__":
    main()
