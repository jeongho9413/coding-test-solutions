# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# strategy: greedy with stack
# time: O(N)
# space: O(N) 
def solution(number, k):
    
    stack = list()
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            
        stack.append(num)
        
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)
