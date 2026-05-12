# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# strategy: BFS
# time: O(N^2 \times L)
# space: O(N)
from collections import deque

def helper(word1, word2):
    cnt = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        curr_word, step = q.popleft()
        
        if curr_word == target:
            return step
        
        for word in words:
            if word not in visited and helper(curr_word, word):
                visited.add(word)
                q.append((word, step + 1))
                
    return 0
