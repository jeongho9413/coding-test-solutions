class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        #
        def binary_search(nums, target, pos_left):
            l, r = 0, len(nums) - 1
            i = -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    i = m

                    if pos_left:
                        r = m - 1
                    else:
                        l = m + 1

            return i

        #
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        return [left, right]
