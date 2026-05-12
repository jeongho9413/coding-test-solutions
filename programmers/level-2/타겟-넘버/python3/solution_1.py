# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# strategy: dfs
# time: O(2^n)
# space: O(N)
def solution(numbers, target):
    
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    return dfs(0, 0)
