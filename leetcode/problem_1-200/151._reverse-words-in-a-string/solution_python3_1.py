class Solution:
    def reverseWords(self, s: str) -> str:

        #
        words = list()
        for word in s.strip().split():
            words.append(word)

        #
        l, r = 0, len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1

        return " ".join(words)
