from logging import root


class Solution:
    def mergeTwoBinaryTree(root1, root2):

        if not root1:
            return root2
        if not root2:
            return root1
