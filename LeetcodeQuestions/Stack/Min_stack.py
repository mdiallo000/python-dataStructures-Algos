class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        topval = 0
        topval = self.pop()
        return topval

    def getMin(self):
        minVal = 0
        minVal = self.stack.pop(0)
