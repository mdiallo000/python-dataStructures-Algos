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

        count_good_nodes = 0
        my_root = res[0]

        for node in res:
            if node >= my_root:
                count_good_nodes += 1

        return count_good_nodes
