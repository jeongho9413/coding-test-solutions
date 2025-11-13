"""
leetcode - 9. palindrome number
approach: using math (remainder)
time: O(n)
space: O(1)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:

        #
        if x < 0:
            return False

        #
        rev, orig = 0, x

        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        return rev == orig
