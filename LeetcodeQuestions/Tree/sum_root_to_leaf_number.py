class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def preorder(node, curr_number):
            nonlocal total
            if node:

                curr_number = curr_number * 10 + node.val

                if not node.left or node.right:
                    total += curr_number

                preorder(node.left, curr_number)
                preorder(node.right, curr_number)

        preorder(root, 0)
        return total

    def alternateMethod(self, root):

        if not root:
            return 0

        res = []

        def dfs(node, curr):

            if not node:
                return
