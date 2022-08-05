from gettext import find


class Solution:

    def sumLeafNodes(root):

        def findMax(node):
            if not node:
                return 0

            if node.left and not node.left.left and not node.right.right:
                return node.left.val + findMax(node.right)
            else:
                return findMax(node.left) + findMax(node.right)

        findMax(root)
