# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# strategy: min-heap
# time: O(N log N)
# space: O(N)
def solution(scoville, K):
    
    import heapq
    
    heapq.heapify(scoville)  # O(N)
    res = 0
    
    while scoville[0] < K:  # O(N)
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)  # O(log N)
        second = heapq.heappop(scoville)
        
        new = first + (second * 2)
        heapq.heappush(scoville, new)  # O(log N)
        
        res += 1
        
    return res
