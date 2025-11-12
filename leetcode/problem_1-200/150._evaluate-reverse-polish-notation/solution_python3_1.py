class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #
        res = deque(list())

        #
        for ch in tokens:
            if ch == "+":
                res.append(res.pop() + res.pop())
            elif ch == "-":
                second = res.pop()
                first = res.pop()
                res.append(first - second)
            elif ch == "*":
                res.append(res.pop() * res.pop())
            elif ch == "/":
                second = res.pop()
                first = res.pop()
                res.append(int(first/second))
            else:
                res.append(int(ch))
        
        return res[0]
