"""
leetcode - 80. remove duplicate from sorted array II
using two pointers
time: O(n)
space: O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #
        n = len(nums)
        l = 2

        #
        for r in range(2, n):
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1

        return l
