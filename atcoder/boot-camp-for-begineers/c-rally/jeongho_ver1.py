import sys
import os
import math

def solution(n: int, arr: list) -> int:
    
    arr_temp = list()
    for p in range(1, 101):
        arr_temp2 = list()
        for x_i in arr:
            arr_temp2.append(( x_i - p ) ** 2)
        arr_temp.append(sum(arr_temp2))
            
    return min(arr_temp)

"""
inputs:
    2
    1 4
outputs:
    5
    
inputs:
    7
    14 14 2 13 56 2 37
outputs:
    2354
"""
n = int(input())
arr = list(map(int, input().split()))
print(solution(n, arr))
