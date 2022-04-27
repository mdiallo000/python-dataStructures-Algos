class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def preorder(node, maxVal):
            if not node:
                return 0

            count_nodes = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, count_nodes)
            count_nodes += preorder(node.left, maxVal)
            count_nodes += preorder(node.right, maxVal)
