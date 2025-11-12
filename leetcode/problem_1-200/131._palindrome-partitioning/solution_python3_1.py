class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #
        res = list()

        #
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        #
        def dfs(start, path):
            if start == len(s):
                res.append(path)
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start : end]):
                    dfs(end, path + [s[start : end]])

        #
        dfs(0, [])
        return res
