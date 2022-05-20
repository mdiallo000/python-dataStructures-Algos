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
        self.left.next = self.right
        self.right.prev = self.left
    # create Helper function that will delete and add new nodes into cache
    def insert(self, node):

    def remove(self, node):

    def get(self, key: int) -> int:
        #  if the key exists we not only return its value we also update it to be the most recently accessed
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.remove(node)
            #  we remove it from its current position since it is being used and we re instate it back in the front of the list since its been recently used
            return node.val
        return -1

    def put(self, key: int, value: int):
