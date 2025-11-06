class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #
        n = len(matrix)
        t = 0
        b = n - 1

        #
        while t < b:
            for c in range(n):
                temp = matrix[t][c]
                matrix[t][c] = matrix[b][c]
                matrix[b][c] = temp
            t += 1
            b -= 1

        #
        for r in range(n):
            for c in range(r + 1, n):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
