class Solution:
    def romanToInt(self, s: str) -> int:

        #
        res = 0
        n = len(s)
        i = 0
        hm = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }

        #
        while i < n:
            if i < n - 1 and hm[s[i]] < hm[s[i + 1]]:
                res += hm[s[i + 1]] - hm[s[i]]
                i += 2
            else:
                res += hm[s[i]]
                i += 1

        return res
