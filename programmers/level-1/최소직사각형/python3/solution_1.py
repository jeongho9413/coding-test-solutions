# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# Strategy: Brute-force
# Time complexity: O(n)
# Space complexity: O(1)
def solution(sizes):
    max_w, max_h = 0, 0
    
    for w, h in sizes:
        longer = max(w, h)
        shorter = min(w, h)
        
        max_w = max(max_w, longer)
        max_h = max(max_h, shorter)
        
    return max_w * max_h
