# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# strategy: Greedy
# time: O(N log N)
# space: O(N)
def solution(routes):
    res = 0
    routes.sort(key=lambda x: x[1])
    last_camera = -30001
    
    for route in routes:
        if route[0] > last_camera:
            res += 1
            last_camera = route[1]
            
    return res
