
from types import NoneType


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStackLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        newItem = Node(data)
        if self.head is None:
            self.head = newItem
            self.tail = newItem

        else:
            self.tail.next = newItem
            self.tail = newItem
            self.length += 1
