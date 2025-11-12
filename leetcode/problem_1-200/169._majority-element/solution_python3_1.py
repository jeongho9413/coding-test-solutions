class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #
        hm = dict()
        res = 0
        maj = 0

        #
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
            if hm[num] > maj:
                res = num
                maj = hm[num]

        return res
