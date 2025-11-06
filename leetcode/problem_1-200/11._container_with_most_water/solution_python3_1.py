class Solution:
    def maxArea(self, height: List[int]) -> int:

        #
        n = len(height)
        res = 0
        l = 0
        r = n - 1

        #
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            res = max(res, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
