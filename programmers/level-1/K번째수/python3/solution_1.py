# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# strategy: sorting
# time: O(M \times N log N)
# space: O(N)
def solution(array, commands):
    res = list()
    
    for command in commands:
        i, j, k = command
        temp = array[i - 1 : j]
        temp.sort()
        res.append(temp[k - 1])
        
    return res
