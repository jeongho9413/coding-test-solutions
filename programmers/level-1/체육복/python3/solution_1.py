# https://school.programSmers.co.kr/learn/courses/30/lessons/42862
# Strategy: Greedy with set difference
# Time: O(n log n)
# Space: O(n)
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    """
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    """
    
    _reserve.sort()
    _lost.sort()
    
    # for r in sorted(_reserve)
    for r in _reserve:
        f = r - 1
        b = r + 1
        
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    
    return n - len(_lost)
