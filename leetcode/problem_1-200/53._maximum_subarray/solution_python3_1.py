class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #
        global_sum = nums[0]
        cur_sum = 0

        #
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            global_sum = max(global_sum, cur_sum)

        return global_sum
