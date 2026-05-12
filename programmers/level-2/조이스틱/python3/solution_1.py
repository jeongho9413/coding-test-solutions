# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# strategy: greedy
# time: O(N)
# space: O(1)
def solution(name):
    
    spell_move = 0
    
    for char in name:
        spell_move += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
    n = len(name)
    min_move = n - 1
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        min_move = min(min_move, 2 * i + n - next_i, i + 2 * (n - next_i))
        
    return spell_move + min_move
