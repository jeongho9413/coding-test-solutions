# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# time: O(N log N)
# space:O(N)
def solution(numbers):
    
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    res = ''.join(numbers)
    
    return str(int(res))
