# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# time complexity: O(N)
# space complexity: O(N)
def solution(s):
    from collections import deque
    
    stack = deque()
    
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
            
    return len(stack) == 0
