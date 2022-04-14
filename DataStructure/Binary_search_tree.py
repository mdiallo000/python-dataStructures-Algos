

from turtle import left


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

    def find_min_node(self):
        curr = self.root
        while curr.left_child:
            curr = curr.left_child
        return curr.data

    def find_max_node(self):
        curr = self.root
        while curr.right_child:
            curr = curr.right_child
        return curr.data

    def get_node_with_parent(self, data):
        parent = None
        current = self.root
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

    def remove(self, data):
        # from our get node with parent function above we can get the node we are interested in removing as well as its parent

        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        # NOW check how many child Nodes are attached to this parent since the number of children determine the approach we will take to solve
        children_count = 0
        # If it exist both a left and a right child then our count is two
        if node.left_child and node.right_child:
            children_count = 2
        #  if no right and no left child exists than the count is zero
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        # Now we can begin the proccess of removing the Nodes, first with a child with no nodes attached
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
        elif children_count == 1:
            grandchild = None

            if node.left_child:
                grandchild = node.left_child
            else:
                grandchild = node.right_child

            if parent:
                if parent.right_child is node:
                    parent.right_child = grandchild
                else:
                    parent.left_child = grandchild
            else:
                self.root = grandchild
        # Now if the child node has two children of its own
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.rigth_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.rigth_child

    def visit(self, node):
        print(node.data)

    def pre_order(self, curr):
        self.visit(curr)
        self.pre_order(curr.left_child)
        self.pre_order(curr.right_child)

    def inorder(self, curr):
        self.pre_order(curr.left_child)
        self.visit(curr)
        self.pre_order(curr.right_child)


#  Binary search Trees are higly efficient due to improved efficiency it provides.
#  Average Insertion, deletion time complexity of O (log n)
#  Access is fast, but cant be slower if its unbalanced.
#  worst-case complexity for searching is 0(n)
#  worst-case complexity for insertion is 0(n)
#  worst-case complexity for deletion is 0(n)
dummy = BST()
dummy.insert_Node(78)
dummy.insert_Node(12)
dummy.insert_Node(45)
dummy.insert_Node(10)
dummy.insert_Node(42)
dummy.insert_Node(8)
dummy.remove(42)
dummy.pre_order()
