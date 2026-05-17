# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# Strategy: Sorting 
# Time: O(n log n)
# Space: O(n)
def solution(citations):
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        if c < i + 1:
            return i
        
    return len(citations)
