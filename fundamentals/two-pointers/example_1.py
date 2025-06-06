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

n = 5                   # 데이터의 개수 N
m = 5                   # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]  # 전체 수열

cnt = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        cnt += 1
    interval_sum -= data[start]
    
print(cnt)
