"""
output:
    18
"""
import sys

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
N = len(nums)
K = 5

temp = sum(nums[:K])
max_v = temp

for i in range(K, N):
    temp += nums[i] - nums[i - K]
    max_v = max(max_v, temp)
    
print(max_v)
