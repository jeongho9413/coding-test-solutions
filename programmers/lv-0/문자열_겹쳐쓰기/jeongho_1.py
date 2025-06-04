"""
https://school.programmers.co.kr/learn/courses/30/lessons/181943
"""

def solution(a: str, b: str, s: int) -> str:
    return f"{a[:s] + b + a[s + len(b):]}"


"""
input: He11oWor1d lloWorl 2
output: HelloWorld
"""
my_string, overwrite_string, s = list(input().strip().split())
my_string, overwrite_string, s = str(my_string), str(overwrite_string), int(s)
print(solution(my_string, overwrite_string, s))
