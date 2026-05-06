# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# strategy: monotonic stack
# time: O(N)
# space: O(N)
def solution(prices):
    
    n = len(prices)
    res = [0] * n
    stack = list()
    
    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        res[j] = n - 1 - j
        
    return res
