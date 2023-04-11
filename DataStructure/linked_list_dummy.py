
#  the goal is to create a linked list data structure as wells as the methods associated with it

class Node:
    #  the node will be the object that will be the foundational building block for our linked list data structure. It will hold info on the data it is storing within the val variable and a reference pointer to the next object in the chain
    def __init__(self, val) -> None:
        self.val = val
        self.next = None