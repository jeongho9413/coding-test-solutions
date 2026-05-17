# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# Strategy: Hashmap
# Time: O(n)
# Space: O(n)
def solution(participant, completion):
    hm = dict()
    
    for p in participant:  # O(n)
        hm[p] = hm.get(p, 0) + 1
        
    for c in completion:  # O(m)
        hm[c] -= 1
        
    for key, val in hm.items():  # O(n)
        if val > 0:
            return key
