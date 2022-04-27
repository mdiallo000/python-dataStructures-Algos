class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def preorder(node, maxVal):
            if not node:
                return 0

            count_good_nodes = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, count_good_nodes)
            count_good_nodes += preorder(node.left, maxVal)
            count_good_nodes += preorder(node.right, maxVal)
            return count_good_nodes

        return preorder(root, root.val)
