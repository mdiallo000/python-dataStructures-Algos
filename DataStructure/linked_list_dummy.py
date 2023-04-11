
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
        #  what if we need to add a node to the end of the list how will we do it
        #  i can think of two scenarios
        #  we need to check if there is a head first probably, if there is no head then we should turn this method call to perform the append_to_tail method
        #  now that we can safely assume that their is already a tail in the list we can then create a new node
        if not self.head:
            self.append_to_head(value)
        else:
            node = Node(value)
            tail.next = node
            tail = node
            self.length += 1

    def get_location(self, index):
        #  now we need to find where within the list a node may be located. with the use of an index we may pinpoint the nodes location by traversing the list until we reach the index position

        curr = self.head
        pos = 0
        while pos != index:
            cur = cur.next
            pos += 1
        return cur

    def insert_node(self, value, index):
        # with this method we are attempting to insert a node within the list.
        #  we can either insert from the head or the tail or in some position that lies within
        pass

    def pop(self):
        pass

    def size(self):
        #  simply return the length of the linked list
        return self.length

    def remove_first_node(self):
        if self.head:
            self.head = self.head.next
            self.length -= 1

    def print_list(self):
        #  printing the list is easy. All we need to do is traverse the list. Add all the node values into an array and then print the array once the traversal is over
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        print(res)
