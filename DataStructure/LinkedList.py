from logging import NullHandler
from traceback import print_tb


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MylinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def Append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def Pop(self):

        lastNode = self.head

        while lastNode.next.next:
            last_node = last_node.next

        last_node.next = None
        self.length += 1

    def size(self):
        return self.length

    def append_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def remove_first_node(self):
        if self.head is not None:

            self.head = self.head.next
            self.length -= 1

    def print_list(self):

        cur = self.head

        while cur:
            print(cur.value)
            cur = cur.next


data = MylinkedList()
data.Append(2554)
data.Append(0.35)
data.Append(7)
data.Append(45)
data.print_list()
