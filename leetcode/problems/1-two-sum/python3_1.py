"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]
            
            if y in h and h[y] != i:
                return [i, h[y]]
