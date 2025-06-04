"""
https://school.programmers.co.kr/learn/courses/30/lessons/181951
"""

def solution(a: int, b: int) -> None:
    print(f"a = {a}\nb = {b}")

"""
input: 
    4, 5
output:
    a = 4
    b = 5
"""
a, b = list(map(int, input().strip().split()))
solution(a, b)
