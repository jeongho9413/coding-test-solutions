class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #
        n = len(nums)
        goal_i = n - 1

        #
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal_i:
                goal_i = i

        return True if goal_i == 0 else False
