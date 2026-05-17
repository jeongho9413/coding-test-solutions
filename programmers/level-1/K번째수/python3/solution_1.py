# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# Strategy: Sorting
# Time: O(m \times n log n)
# Space: O(n)
def solution(array, commands):
    res = list()
    
    for command in commands:  # O(m)
        i, j, k = command
        temp = array[i - 1 : j]
        temp.sort()  # O(n log n)
        res.append(temp[k - 1])
        
    return res
