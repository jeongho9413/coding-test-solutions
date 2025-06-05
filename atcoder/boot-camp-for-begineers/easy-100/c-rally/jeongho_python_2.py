import sys
import os
import math

def solution(n: int, arr: list) -> int:
    
    result = min(
        sum((x_i - p) ** 2 for x_i in arr) for p in range(1, 101)
    )
            
    return result

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
