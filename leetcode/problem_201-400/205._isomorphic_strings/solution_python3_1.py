class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        #
        if len(s) != len(t):
            return False
        
        #
        hm_s = dict()
        hm_t = dict()

        #
        for i in range(len(s)):
            if s[i] not in hm_s:
                hm_s[s[i]] = i
            if t[i] not in hm_t:
                hm_t[t[i]] = i
            if hm_s[s[i]] != hm_t[t[i]]:
                return False

        return True
