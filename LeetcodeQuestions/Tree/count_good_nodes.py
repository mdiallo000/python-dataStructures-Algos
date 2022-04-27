class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def preorder(node):
            if not node:
                return
