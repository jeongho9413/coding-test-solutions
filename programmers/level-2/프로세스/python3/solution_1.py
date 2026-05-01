# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# time complexity: O(N^2)
# space complexity: O(N)
def solution(priorities, location):
    from collections import deque
    
    res = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    
    while queue:
        current = queue.popleft()
        
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            res += 1
            if current[0] == location:
                return res
