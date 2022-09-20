from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.storage = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:

    def get(self, key: str, timestamp: int) -> str:
