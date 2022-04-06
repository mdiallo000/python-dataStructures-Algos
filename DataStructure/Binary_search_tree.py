

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

    def find_Node(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right_child:
            return self._find(data, cur_node.right_child)
        elif data < cur_node.data and cur_node.left_child:
            return self._find(data, cur_node.left_child)
        if data == cur_node.data:
            return True


dummy = BST()
dummy.insert_Node(78)
dummy.insert_Node(12)
dummy.insert_Node(45)
dummy.insert_Node(10)
dummy.insert_Node(42)
dummy.insert_Node(8)
print(dummy.find_Node(89))
