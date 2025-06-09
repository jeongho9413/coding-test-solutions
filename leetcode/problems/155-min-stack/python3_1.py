"""
155. Min Stack
https://leetcode.com/problems/min-stack/

idea(algorithm):
    -
time complexity:
    -
memory complexity:
    -
data structure:
    -
"""
class MinStack:
    def __init__(self):
        self.data = []
        self.mins = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
