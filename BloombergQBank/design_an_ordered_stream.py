class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.position = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.stream[idKey - 1] = value
        while self.position < len(self.stream) and self.stream[self.position] != None:
            res.append(self.stream[self.position])
            self.position += 1
        return res
