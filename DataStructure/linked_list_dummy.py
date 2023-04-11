
#  the goal is to create a linked list data structure as wells as the methods associated with it

class Node:
    #  the node will be the object that will be the foundational building block for our linked list data structure. It will hold info on the data it is storing within the val variable and a reference pointer to the next object in the chain
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    # the linked list will need to know where the head of the list as well as the tail is located. Each instance of that

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append_to_head(self, value):
        #     so now we are trying to add a node to the head of the linked list
        #  we can have two scenarios, one where the head is currently empty then in that case we would just set the head to point at the new node. Scenario two is the head is already occupied and we need to make the new node point at the head and then move the head pointer to be with the new node
        if not self.head:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length += 1
        else:

            node = Node(value)
            node.next = self.head
            self.head = node
            self.length += 1

    def append_to_tail(self, value):
        pass

    def get_location(self, index):
        pass

    def insert_node(self, value, index):

        pass

    def pop(self):
        pass

    def size(self):
        pass

    def remove_first_node(self):
        pass

    def print_list(self):
        pass
