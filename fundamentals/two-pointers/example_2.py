"""
개발자 창고 | 코딩테스트 알고리즘 - 5. 투포인터
https://www.youtube.com/watch?v=U0TXIFiCIu0
https://www.acmicpc.net/problem/2559

개념:
    각 원소마다 모든 값을 순회해야할 때 O(N^2)
    연속하다는 특성을 이용해서 처리 O(N)
    두 개의 포인터(커서)가 움직이면서 계산
    처음부터 생각하기 어려움, 쉬운 방법부터 생각

live coding:
    idae:
        투 포인터 활용
        for문으로, 처음에 k개 값을 저장
        다음 인덱스 더해주고, 이전 인덱스를 빼줌
        이 때마다 최댓값을 갱신
    time complexity:
        O(N) = 1e5 > 가능
    data structure:
        각 숫자들 N개 저장 배열: int[]
            숫자들 최대 100 > INT 가능
        최댓값
""" 
import sys

"""
input:
    10 2
    3 -2 -4 -9 0 3 7 13 8 -3
output:
    21
"""
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

temp = 0 
for k in range(K):
    temp += nums[k]
    
max_value = temp
for i in range(K, N):
    temp += nums[i]
    temp -= nums[i - K]
    max_value = max(max_value, temp)
    
print(max_value)
