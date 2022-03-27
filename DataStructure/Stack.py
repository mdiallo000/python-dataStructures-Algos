

from hashlib import new


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
            print(cur.data)
            cur = cur.next

    def push(self, data):
        newItem = Node(data)
        if self.head is None:
            self.head = newItem
            self.tail = newItem

        else:
            newItem.next = self.head
            self.head = newItem
            self.length += 1

    def pop(self):
        if self.head is not None:
            sec_last = self.head
            last_item = sec_last
            while last_item:
                sec_last = last_item
                last_item = last_item.next

            self.tail = sec_last
            sec_last.next = None
        return last_item


myStack = MyStackLinkedList()

myStack.push(56)
myStack.push(452)
myStack.push(156)
myStack.push(6)
myStack.print_stack()
