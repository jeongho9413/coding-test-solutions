# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    
    hm = dict()
    
    for p in participant:  # O(N)
        hm[p] = hm.get(p, 0) + 1
        
    for c in completion:  # O(M)
        hm[c] -= 1
        
    for key, val in hm.items():  # O(N)
        if val > 0:
            return key
    # answer = ''
    # return answer
