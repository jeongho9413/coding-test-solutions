class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #
        n = len(board)
        rows = [[False] * n for _ in range(n)]
        cols = [[False] * n for _ in range(n)]
        boxes = [[False] * n for _ in range(n)]

        #
        for r in range(n):
            for c in range(n):
                if board[r][c] != ".":
                    num = ord(board[r][c]) - ord("1")
                    i = (r // 3) * 3 + (c // 3)

                    if rows[r][num] or cols[c][num] or boxes[i][num]:
                        return False
                    else:
                        rows[r][num] = cols[c][num] = boxes[i][num] = True

        return True
