class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #
        hm = dict()

        #
        for s in strs:
            s_temp = tuple(sorted(s))
            if s_temp not in hm:
                hm[s_temp] = list()
            hm[s_temp].append(s)

        return list(hm.values())
