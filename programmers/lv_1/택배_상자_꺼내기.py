def solution(n: int, w:int, num: int) -> int:
    answer = 0
    
    row = (num - 1) // w
    idx = (num - 1) % w
    col = idx if row % 2 == 0 else w - 1 - idx
    
    top = (n - 1) // w
    last_cnt = n - (top * w)
    
    for r in range(row + 1, top + 1):
        if r < top:
            answer += 1
        else:
            if last_cnt == 0:
                answer += 1
            else:
                if (r % 2 == 0 and col < last_cnt) or (r % 2 == 1 and col >= w - last_cnt):
                    answer += 1
    return answer + 1
