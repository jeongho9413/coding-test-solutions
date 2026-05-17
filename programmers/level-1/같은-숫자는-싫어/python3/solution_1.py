# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# Strategy: Iteration
# Time complexity: O(n)
# Space complexity: O(n)
def solution(arr):
    res = list()
    
    for num in arr:
        if not res or res[-1] != num:
            res.append(num)
            
    return res
