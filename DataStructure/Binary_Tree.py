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

    def addChild(self, BinaryTree):
        self.children.append(BinaryTree)


tree = BinaryTree("Uefa", [])
ucl = BinaryTree('Champions League', [])
uel = BinaryTree('Europe League', [])
tree.addChild(ucl)
tree.addChild(uel)
groupA = BinaryTree('Group A', [])
teams = BinaryTree('Man,BFC,SPL,PSV', [])
groupA.addChild(teams)
ucl.addChild(groupA)
print(tree)
