class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def preorder(node):
            if not node:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        count_good_nodes
