"""
sorting - insertion sort
"""
import os
import sys
from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

def main() -> None:
    arr = list(map(int, input().split()))
    print(insertion_sort(arr))
    
if __name__ == "__main__":
    main()
