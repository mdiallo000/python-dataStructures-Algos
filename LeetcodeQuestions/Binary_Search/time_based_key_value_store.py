from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.storage = defaultdict(SortedDict())

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.storage[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.storage:
            return ''

        for curr in reversed(range(1, timestamp + 1)):
            if curr in self.storage[key]:
                return self.storage[key][curr]

        return ""
