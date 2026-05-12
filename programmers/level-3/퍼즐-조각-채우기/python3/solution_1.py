# https://school.programmers.co.kr/learn/courses/30/lessons/84021
# Strategy: Simulation with BFS
# Time: O(N^2 + M \times P \times 4 \times K)
# Space: O(N^2)
from collections import deque

def find_blocks(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    blocks = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                curr_block = [(i, j)]
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            curr_block.append((nx, ny))
                            
                blocks.append(normalize(curr_block))
                
    return blocks

def normalize(block):
    min_x = min(p[0] for p in block)
    min_y = min(p[1] for p in block)
    
    return sorted([(x - min_x, y - min_y) for x, y in block])

def rotate(block):
    rotated = [(y, -x) for x, y in block]
    
    return normalize(rotated)

def solution(game_board, table):
    blank_spaces = find_blocks(game_board, 0)
    puzzle_pieces = find_blocks(table, 1)
    
    res = 0
    used_piece = [False] * len(puzzle_pieces)
    
    for blank in blank_spaces:
        found = False
        for i, piece in enumerate(puzzle_pieces):
            if used_piece[i]:
                continue
                
            curr_piece = piece
            for _ in range(4):
                if blank == curr_piece:
                    res += len(blank)
                    used_piece[i] = True
                    found = True
                    break
                curr_piece = rotate(curr_piece)
                
            if found:
                break
                
    return res
