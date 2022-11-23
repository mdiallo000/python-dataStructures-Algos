class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for n in range(len(nestedList)-1, -1, -1):
            self.stack.append(nestedList[n])

    def next(self) -> int:

    def hasNext(self) -> bool:
