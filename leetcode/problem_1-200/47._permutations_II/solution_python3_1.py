class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        #
        n = len(nums)
        res = set()

        #
        def dfs(perm, used):
            if len(perm) == n:
                res.add(tuple(perm))
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
        return list(res)
