# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# time complexity: O(N logN)
def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    
    for i in range(n - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
        
    return True
