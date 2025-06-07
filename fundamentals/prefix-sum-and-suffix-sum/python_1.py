"""
다빈치코딩 | [알고리즘] 구간 합, 누적 합(Prefix Sum) 알고리즘 문제 풀이
https://www.youtube.com/watch?v=QaOeON30txU

구간 합 구하기 4
https://www.acmicpc.net/problem/11659
"""
import sys
# import collections

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

sum_arr = []
temp = 0
for i in range(N + 1):
    temp += arr[i]
    sum_arr.append(temp)
    
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i - 1])
