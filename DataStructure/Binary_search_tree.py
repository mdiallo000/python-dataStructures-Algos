
from readline import insert_text


class Node:
    def __init__(self, value):

        self.value = value
        self.right_child = None
        self.left_child = None

    def insert_node(rootnode, value):
        # First chech if a root even exists, if it doesnt, make one
        if rootnode.value == None:
            rootnode.value = value
    # Next we check the value if its less than the root we need to add it to the left
        elif value <= rootnode.value:
            if rootnode.left_child == None:
                rootnode.left_child = Node(value)
            else:
                insert_node(rootnode.left_child, value)

    # If the value is greater that means we go towards the right side
        else:
            if rootnode.right_child == None:
                rootnode.right_child = Node(value)
            else:
                insert_node(rootnode.right_child, value)
        print('A node has been succesfully added')
