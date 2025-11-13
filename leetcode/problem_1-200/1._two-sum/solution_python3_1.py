"""
leetcode - 1. two sum
approach: using a hashmap
time: O(n)
space: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #
        hm = dict()

        #
        for i, num in enumerate(nums):
            if target - num in hm:
                return [i, hm[target - num]]
            else:
                hm[num] = i
