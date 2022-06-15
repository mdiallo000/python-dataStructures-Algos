class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.position = 0

    def insert(self, idKey: int, value: str) -> List[str]:
