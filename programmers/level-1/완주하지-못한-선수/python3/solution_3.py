# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# strategy: sorting
# time: O(N log N)
# space: O(N)
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
        
    return participant[-1]
