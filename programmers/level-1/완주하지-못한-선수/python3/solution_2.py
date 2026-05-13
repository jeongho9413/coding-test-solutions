# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# Strategy: Hashmap using Counter
# Time: O(n) 
# Space: O(n)
from collections import Counter

def solution(participant, completion):
    
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    res = list((p_counter - c_counter).keys())[0]
    
    return res
