# Think of a queue as analogous to the line people form whjen purchasing Items or attempting to gain entry into a place. Or think of a car wash, the first car in will be the first car out

# FIFO: First In, First out.

from re import M


class QueueArray:

    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        item = self.items[0]
        self.items.pop(0)
        return item

    def print_items(self):
        # if self.items != []:
        for i in self.items:
            print(i)

    def is_empty(self):
        if self.items == []:
            return True
        return False

    def size(self):
        print(len(self.items))


# Bellow I will attempt to do one with an array.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queuelist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def dequeue(self):
        if self.head:
            currentHead = self.head
            self.head = self.head.next
        self.length -= 1
        return currentHead.data

    def print_queue(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def size(self):
        return self.length

    def is_empty(self):
        return True if self.length == 0 else False


line = Queuelist()
line.enqueue(45)
line.enqueue(78)
line.enqueue(450)
line.enqueue(5)
line.dequeue()
line.dequeue()
line.dequeue()
line.dequeue()
line.enqueue('new item')
line.enqueue('second item')
line.dequeue()
line.dequeue()

line.print_queue()
print(line.size())
print(line.is_empty())
