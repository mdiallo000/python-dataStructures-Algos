#  we need to account for the fact


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else 0)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
