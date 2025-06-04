"""
https://school.programmers.co.kr/learn/courses/30/lessons/181945
"""

def solution(str_1: str) -> None:
    for i in range(len(str_1)):
        print(f"{str_1[i]}")
        
"""
input:
    abcde
output:
    a
    b
    c
    d
    e
"""
solution(str(input().strip()))
