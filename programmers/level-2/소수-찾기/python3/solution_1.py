# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# strategy: brute-force using prime and permutation
# time: O(n! \times \sqrt{K})
# space: O(n!)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    
    from itertools import permutations
    
    n = len(numbers) + 1
    all_numbers = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(list(numbers), i)
        for p in perms:
            num = int(''.join(p))
            all_numbers.add(num)
            
    cnt = 0
    for number in all_numbers:
        if is_prime(number):
            cnt += 1
            
    return cnt
