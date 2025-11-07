class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #
        if not intervals:
            return []

        #
        res = list()
        intervals.sort(key = lambda x: x[0])
        prev = intervals[0]

        #
        for cur in intervals[1:]:
            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(prev)
                prev = cur

        res.append(prev)
        return res
