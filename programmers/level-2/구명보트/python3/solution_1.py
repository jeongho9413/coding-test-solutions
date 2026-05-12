# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# strategy: greedy with two-pointer
# time: O(N log N)
# space: O(N)
def solution(people, limit):
    
    people.sort()
    
    l, r, res = 0, len(people) - 1, 0
    
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        
        r -= 1
        res += 1
        
    return res
