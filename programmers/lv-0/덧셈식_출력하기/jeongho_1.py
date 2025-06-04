"""
https://school.programmers.co.kr/learn/courses/30/lessons/181947
"""

def solution(a: int, b: int) -> int: print(f"{a} + {b} = {a + b}")

"""
input:
    4 5
output:
    4 + 5 = 9
"""
a, b = list(map(int, input().strip().split()))
solution(a, b)
