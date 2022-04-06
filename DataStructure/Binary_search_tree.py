

class Node:
    def __init__(self, data):

        self.data = data
        self.right_child = None
        self.left_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert_Node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):

        if data < cur_node.data:
            if cur_node.left_child is None:
                cur_node.left_child = Node(data)
            else:
                self._insert(data, cur_node.left_child)

        elif data > cur_node.data:
            if cur_node.right_child is None:
                cur_node.right_child = Node(data)
            else:
                self._insert(data, cur_node.right_child)
        else:
            print("No Duplicates Allowed")
