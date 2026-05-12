# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# strategy: brute-force with permutation
# time: O(N \times N!)
# space: O(N)
# 재귀함수(DFS 및 backtracking)를 이용해서 풀기 가능
def solution(k, dungeons):
    
    from itertools import permutations
    
    max_dungeons = 0
    
    for p in permutations(dungeons):
        current_k = k
        cnt = 0
        
        for need, cost in p:
            if current_k >= need:
                current_k -= cost
                cnt += 1
            else:
                break
                
        max_dungeons = max(max_dungeons, cnt)
    
        if max_dungeons == len(dungeons):
            return max_dungeons
        
    return max_dungeons
