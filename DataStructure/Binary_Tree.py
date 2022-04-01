#  A binary search Tree is an hierichal abstract data structure which offers some Unique benefits.

class BinaryTree:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
