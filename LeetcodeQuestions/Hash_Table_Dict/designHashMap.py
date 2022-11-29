class Buckect:
    def __init__(self) -> None:
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False


class MyHashMap:

    def __init__(self):
        pass

    def put(self, key: int, value: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def remove(self, key: int) -> None:
        pass
