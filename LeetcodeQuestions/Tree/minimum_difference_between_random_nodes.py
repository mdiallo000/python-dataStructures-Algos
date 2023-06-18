# Find the minimum difference between two nodes in the binary search tree
class Solution:

    def findMinDifference(root):
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
