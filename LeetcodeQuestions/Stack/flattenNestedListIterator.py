class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for n in range(len(nestedList)-1, -1, -1):
            self.stack.append(nestedList[n])

    def next(self) -> int:

        for elem in self.stack:
            if self.stack and self.stack[-1] == int:
                return self.stack.pop()

    def hasNext(self) -> bool:
        return self.stack
