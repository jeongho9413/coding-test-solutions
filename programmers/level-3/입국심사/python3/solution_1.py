# https://school.programmers.co.kr/learn/courses/30/parts/12486
# Strategy: Parametric Search / Binary Search
# Time: O(L \times log R)
# Space: O(1)
# Similar problems: 
# 입국심사 | https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 징검다리 | https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 예산 | https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 징검다리 건너기 | https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 금과 은 운반하기 | https://school.programmers.co.kr/learn/courses/30/lessons/86053
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
