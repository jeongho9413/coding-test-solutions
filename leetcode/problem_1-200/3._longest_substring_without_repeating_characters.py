class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #
        hs = set()
        l = 0
        res = 0

        #
        for r, ch in enumerate(s):
            while ch in hs:
                hs.remove(s[l])
                l += 1
            hs.add(ch)
            res = max(res, r - l + 1)

        return res
