class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def preorder(node, curr_number):
            nonlocal total
            if node:

                curr_number = curr_number * 10 + node.val

                if not node.left or node.right:
