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

    def append_to_tail(self, value):
        newNode = Node(value)
        if self.head is None:

            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def get_location(self, index):
        counter = 0
        target_position = self.head
        while (counter != index):
            target_position = target_position.next
            counter += 1
        return target_position

    def insert_node(self, value, index):
        new_node = Node(value)
        if index == 0:
            return self.append_to_head(value)

        if index == self.length:
            return self.append_to_tail(value)

        back_node = self.get_location(index - 1)
        new_node.next = back_node.next
        back_node.next = new_node
        self.length += 1

    def pop(self):

        lastNode = self.head

        while lastNode.next.next:
            last_node = last_node.next

        last_node.next = None
        self.length -= 1

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
