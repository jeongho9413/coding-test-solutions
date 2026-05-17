# https://school.programmers.co.kr/learn/courses/30/lessons/12899
# Strategy: Ternary numeral system
# Time: O(log_3 n)
# Space: O(log_3 n)
def solution(n):
    digits = ['4', '1', '2']
    res = ''
    
    while n > 0:
        remainder = n % 3
        n = (n - 1) // 3
        
        res = digits[remainder] + res
    
    return res
