class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capicity = capacity
        self.right, self.left = Node(0, 0), Node(0, 0)

    def get(self, key: int) -> int:

    def put(self, key: int, value: int):
