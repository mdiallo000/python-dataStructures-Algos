# Think of a queue as analogous to the line people form whjen purchasing Items or attempting to gain entry into a place. Or think of a car wash, the first car in will be the first car out

# FIFO: First In, First out.

class QueueArray:
    def __init__(self):
        self.items = []

    def append_elem(self, data):
        self.items.append(data)

    def remove(self):
        item = self.items[0]
        self.items.pop(0)
        return item

    def print_items(self):
        for i in self.items:
            print(i)


myQueue = QueueArray()
myQueue.append_elem("first added: 1")
myQueue.append_elem(45)
myQueue.append_elem(123)
myQueue.append_elem(78)
myQueue.append_elem(5)
myQueue.append_elem('last added: 0')
myQueue.print_items()
myQueue.remove()
# myQueue.remove()
# myQueue.remove()
# myQueue.remove()
# myQueue.remove()
print('AFTER REMOVE METHODE')
myQueue.print_items()
