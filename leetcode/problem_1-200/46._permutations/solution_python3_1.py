class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #
        n = len(nums)
        res = list()

        #
        def dfs(perm, used):
            if len(perm) == n:
                res.append(perm.copy())
                return

            for i in range(n):
                if not used[i]:
                    perm.append(nums[i])
                    used[i] = True
                    dfs(perm, used)
                    perm.pop()
                    used[i] = False

        #
        dfs([], [False] * n)
        return res
