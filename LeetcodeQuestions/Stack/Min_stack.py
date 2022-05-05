#  we need to account for the fact


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else 0)

    def pop(self):
        self.stack.pop()

    def top(self):
        topval = 0
        topval = self.pop()
        return topval

    def getMin(self):
        minVal = 0
        minVal = self.stack.pop(0)
