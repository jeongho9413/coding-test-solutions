"""
https://school.programmers.co.kr/learn/courses/30/lessons/181944
"""

def solution(a: int) -> None:
    if a % 2 == 0: print(f"{a} is even")
    else: print(f"{a} is odd")
    
"""
input:
    100
output:
    100 is even
"""
solution(int(input().strip()))
