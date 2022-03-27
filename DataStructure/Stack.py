

from hashlib import new


class Stack_Node:
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
        newItem = Stack_Node(data)
        if self.head is None:
            self.head = newItem
            self.tail = newItem
            self.length += 1

        else:
            newItem.next = self.head
            self.head = newItem
            self.length += 1

    def pop(self):
        if self.head:
            current_head = self.head
            self.head = current_head.next
        self.length -= 1
        return current_head

    def size(self):
        return print(self.length)

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def peek(self):
        if self.head:
            return self.head.data


myStack = MyStackLinkedList()

myStack.push("I am at the bottom")
myStack.push(452)
myStack.push(98)
myStack.push(112)
myStack.push(78)
myStack.push(6)
myStack.push('oldhead')
myStack.push('I am at the top')
myStack.pop()
print(myStack.is_empty())

print(f'value:{myStack.peek()}')

myStack.print_stack()
