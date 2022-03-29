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


myQueue = QueueArray()
# myQueue.enqueue("first added: 1")
# myQueue.enqueue(45)
# myQueue.enqueue(123)
# myQueue.enqueue(78)
# myQueue.enqueue(5)
# myQueue.enqueue('last added: 0')
myQueue.print_items()
print(myQueue.is_empty())
myQueue.size()
