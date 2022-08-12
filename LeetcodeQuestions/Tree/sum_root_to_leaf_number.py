class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def preorder(node, curr_number):
