"""
https://school.programmers.co.kr/learn/courses/30/lessons/181946
"""

def solution(a: str, b: str) -> None:
    print(f"{a}{b}")
    
"""
input:
    apple pen
output:
    applepen
"""
a, b = list(map(str, input().strip().split()))
solution(a, b)
