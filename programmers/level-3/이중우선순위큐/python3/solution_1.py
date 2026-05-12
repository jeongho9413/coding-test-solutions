# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# strategy: min- and max-heap
# time: O(N log N)
# space: O(N)
def solution(operations):
    
    import heapq
    
    min_heap, max_heap = list(), list()
    visited = [False] * len(operations)
    
    for i, op in enumerate(operations):
        command, val = op.split()
        val = int(val)
        
        if command == 'I':
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True
        elif val == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        else:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
                
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    if not min_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
