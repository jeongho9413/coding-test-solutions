import sys
import os
import math

def solution(a: int, b: int) -> int:
    if a >= b:
        return 1
    else:
        return math.ceil((b - a)/(a - 1)) + 1

"""
inputs: 4, 10
outputs: 3
"""    
a, b = list(map(int, input().split()))
print(solution(a, b))
