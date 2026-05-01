# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# time complexity: O(N \times L)
def solution(phone_book):
    hm = {number: True for number in phone_book}
    
    for phone_number in phone_book:
        prefix = ""
        for digit in phone_number[:-1]:
            prefix += digit
            if prefix in hm:
                return False
            
    return True
