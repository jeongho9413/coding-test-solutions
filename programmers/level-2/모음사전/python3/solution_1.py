# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# strategy: brute-force with product
# time: O(5^k)
# space: O(5^k)
def solution(word):
    
    from itertools import product
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = list()
    
    for i in range(1, 6):
        for p in product(vowels, repeat=i):
            dictionary.append(''.join(p))
            
    dictionary.sort()  # O(N log N)
    
    return dictionary.index(word) + 1  # O(N)
