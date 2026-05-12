# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# strategy: min-heap
# time: O(N^2)
# space: O(N)
def solution(jobs):
    
    import heapq
    
    res, now, i = 0, 0, 0
    start = -1
    heap = list()
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
                
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            res += (now - current[1])
            i += 1
        else:
            now += 1
            
    return res // len(jobs)
