# https://school.programmers.co.kr/learn/courses/30/lessons/389478
# Strategy: Mathematical coordinate mapping with a zigzag pattern
# Time: O(n)
# Space: O(1)
def solution(n, w, num):
    
    def get_col(box):
        row = (box - 1) // w
        mod = (box - 1) % w
        if row % 2 == 0:
            return mod
        else:
            return w - 1 - mod
        
    target_col = get_col(num)
    res = 0
    
    for box in range(num, n + 1):
        if get_col(box) == target_col:
            res += 1
            
    return res
