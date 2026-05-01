# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# time complexity: O(N)
# space complexity: O(K), where K is the number of kinds
def solution(clothes):
    hm = dict()
    for name, kind in clothes:
        hm[kind] = hm.get(kind, 0) + 1
        
    res = 1
    for value in hm.values():
        res *= (value + 1)
        
    return res - 1
