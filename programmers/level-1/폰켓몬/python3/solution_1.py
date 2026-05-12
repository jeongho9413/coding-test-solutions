# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# strategy: hashset
# time: O(N)
# space: O(N)
def solution(nums):
    
    max_pick = len(nums) // 2
    unique_types = len(set(nums))  # time: O(N)
    
    return min(max_pick, unique_types)
