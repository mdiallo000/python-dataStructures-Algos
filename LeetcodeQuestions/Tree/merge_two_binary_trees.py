from logging import root


class Solution:
    def mergeTwoBinaryTree(root1, root2):

        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2

        root1.left = self.mergeTwoBinaryTree(root1.left, root2.left)
        root1.right = self.mergeTwoBinaryTree(root1.right, root2.right)

        return root1
