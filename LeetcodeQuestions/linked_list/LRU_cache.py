class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    # create Helper function that will delete and add new nodes into cache

    def insert(self, node):
        previous = self.right.prev
        node.prev = previous
        node.next = self.right
        previous.next = node
        self.right.prev = node

    def remove(self, node):
        previous, nextNode = node.prev, node.next
        previous.next, nextNode.prev = nextNode, previous

    def get(self, key: int) -> int:
        #  if the key exists we not only return its value we also update it to be the most recently accessed
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int):

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # if we go over the allowed capacity of our cache then we need to remove the LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
