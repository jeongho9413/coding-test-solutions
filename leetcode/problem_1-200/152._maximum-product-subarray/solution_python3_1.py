class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #
        res = max(nums)
        cur_max = 1
        cur_min = 1

        #
        for num in nums:
            temp = cur_max * num
            cur_max = max(temp, num, cur_min * num)
            cur_min = min(temp, num, cur_min * num)
            res = max(res, cur_max)

        return res
