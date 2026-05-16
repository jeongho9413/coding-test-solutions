# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# Strategy: Top-down DP with memoization/caching
# Time: O(3^8)
# Space: O(1)
def solution(N, number):
    if N == number:
        return 1
    
    cache = [None] * 9
    
    def dfs(k):
        if k == 1:
            return {N}
        
        if cache[k] is not None:
            return cache[k]
        
        res_set = set()
        res_set.add(int(str(N) * k))
        
        for j in range(1, k):
            set1 = dfs(j)
            set2 = dfs(k - j)
            
            for op1 in set1:
                for op2 in set2:
                    res_set.add(op1 + op2)
                    res_set.add(op1 - op2)
                    res_set.add(op1 * op2)
                    if op2 != 0:
                        res_set.add(op1 // op2)
                        
        cache[k] = res_set
        return cache[k]
    
    for k in range(1, 9):
        if number in dfs(k):
            return k
        
    return -1
