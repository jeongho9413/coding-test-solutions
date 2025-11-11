class Solution:
    def isPalindrome(self, s: str) -> bool:

        #
        temp = list()
        for word in s:
            if word.isalnum():
                temp.append(word.lower())

        s = "".join(temp)
        l, r = 0, len(s) - 1

        #
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
