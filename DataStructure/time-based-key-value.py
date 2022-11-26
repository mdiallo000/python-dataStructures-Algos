from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
