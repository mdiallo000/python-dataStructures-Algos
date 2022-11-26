from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
