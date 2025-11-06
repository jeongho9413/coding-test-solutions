class Solution:
    def isValid(self, s: str) -> bool:

        #
        q = deque()
        hm = {
            ")" : "(", 
            "]" : "[", 
            "}" : "{"
        }

        #
        for ch in s:
            if ch in hm:
                if q and q[-1] == hm[ch]:
                    q.pop()
                else:
                    return False
            else:
                q.append(ch)
        
        return True if not q else False
