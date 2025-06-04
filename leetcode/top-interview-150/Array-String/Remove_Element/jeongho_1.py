"""
https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List 

class Solution:
    def removeElement(self, nums: List[int], val: int):
        
        self.nums = nums
        self.val = val
        
        k = 0
        for i in range(len(self.nums)):
            if self.nums[i] != self.val:
                self.nums[k] = self.nums[i]
                k += 1
        return k
