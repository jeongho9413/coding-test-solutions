class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #
        global_min = float("inf")
        res = 0

        #
        for p in prices:
            global_min = min(global_min, p)
            res = max(res, p - global_min)

        return res
