# https://school.programmers.co.kr/learn/courses/30/lessons/12969
# Strategy: Iteration
# Time: O(n \times m)
# Space: O(1)
n, m = map(int, input().strip().split(' '))

for _ in range(m):
    print('*' * n)
