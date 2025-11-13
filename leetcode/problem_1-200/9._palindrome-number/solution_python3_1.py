"""
leetcode - 9. palindrome number
approach: using built-in function
time: O(n)
space: O(n)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:

        #
        return str(x) == str(x)[::-1]
