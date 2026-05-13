# https://school.programmers.co.kr/learn/courses/30/parts/12486
# Strategy: Parametric Search / Binary Search
# Time: O(L \times log R)
# Space: O(1)
def solution(n, times):
    
    l, r = 1, max(times) * n
    res = r
    
    while l <= r:
        m = (l + r) // 2
        
        people = 0
        for t in times:
            people += m // t
            
            if people >= n:
                break
                
        if people >= n:
            res = m
            r = m - 1
        else:
            l = m + 1
            
    return res
