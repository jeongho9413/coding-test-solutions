def solution(n, w, num):
    
    #
    row = (num - 1) // w
    idx = (num - 1) % w
    col = idx if row % 2 == 0 else w - idx - 1
    
    top = (n - 1) // w
    last_cnt = n - (top * w)
    res = 0
    
    #
    for r in range(row + 1, top + 1):
        if r < top:
            res += 1
        else:
            if last_cnt == 0:
                res += 1
            else:
                if r % 2 == 0 and col < last_cnt:
                    res += 1
                elif r % 2 == 1 and col >= w - last_cnt:
                    res += 1
    
    return res + 1
