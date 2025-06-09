"""
C - Next Prime
https://atcoder.jp/contests/abc149/tasks/abc149_c

idea(algorithm):
    2보다 작은 수는 소수X
    2 자체는 소수
    짝수는 소수X
    3부터 isqrt()까지 홀수만 나누어 떨어지는지 검사
time complexity:
    -
memory complexity:
    -
data structure:
    -
"""
import sys
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
        
    return True

def main() -> None:
    x = int(input())
    while not is_prime(x):
        x += 1
    print(x)
    
if __name__ == "__main__": 
    main()
