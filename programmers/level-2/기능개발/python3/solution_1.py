# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# time complexity: O(N)
# space complexity: O(N)
def solution(progresses, speeds):
    import math
    
    res = list()
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    deploy_day = days[0]
    cnt = 0
    
    for day in days:
        if day > deploy_day:
            res.append(cnt)
            deploy_day = day
            cnt = 1
        else:
            cnt += 1
            
    res.append(cnt)
    return res
