class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        #
        rows = len(matrix)
        cols = len(matrix[0])
        x, y = 0, 0
        dx, dy = 1, 0
        res = list()

        #
        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == ".":
              dx, dy = -dy, dx

            x += dx
            y += dy

        return res  
