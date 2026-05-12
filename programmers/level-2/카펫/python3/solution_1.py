# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# strategy: brute-force
# time: O(\sqrt{total})
# space: O(1)
def solution(brown, yellow):
    
    total = brown + yellow
    
    for h in range(3, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
