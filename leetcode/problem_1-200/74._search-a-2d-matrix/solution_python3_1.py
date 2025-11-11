"""
leetcode - 74. search a 2D matrix
using a binary search
time: O(log m + log n)
space: O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #
        t = 0
        b = len(matrix) - 1

        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] < target < matrix[m][-1]:
                break
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1

        #
        row = (t + b) // 2
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1

        return False
