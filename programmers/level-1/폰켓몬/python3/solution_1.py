# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# Strategy: Hashset
# Time: O(n)
# Space: O(n)
def solution(nums):
    max_pick = len(nums) // 2
    unique_types = len(set(nums))  # O(n)
    
    return min(max_pick, unique_types)
