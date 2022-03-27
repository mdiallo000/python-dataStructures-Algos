
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

    def print_stack(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    def push(self, data):
        newItem = Node(data)
        if self.head is None:
            self.head = newItem
            self.tail = newItem

        else:
            self.tail.next = newItem
            self.tail = newItem
            self.length += 1


myStack = MyStackLinkedList()

myStack.push(56)
myStack.push(452)
myStack.push(156)
myStack.push(6)
myStack.print_stack()
