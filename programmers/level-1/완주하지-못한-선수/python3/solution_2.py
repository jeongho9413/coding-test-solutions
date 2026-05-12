# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# strategy: hashmap
# time complexity: 
# space complexity: 
def solution(participant, completion):
    
    from collections import Counter
    
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    res = list((p_counter - c_counter).keys())[0]
    
    return res
