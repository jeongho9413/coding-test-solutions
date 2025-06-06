"""
특정한 합을 가지는 부분 연속 수열 찾기: 코드 예시 (Python)
https://www.youtube.com/watch?v=ttLRltNDiCo&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=39

brute force = 완전 탐색
    O(N^2)

two pointers
    O(N)
""" 
# import sys
# import math

n = 5
m = 5
data = [1, 2, 3, 2, 5]

cnt = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        cnt += 1
    interval_sum -= data[start]
    
print(cnt)
