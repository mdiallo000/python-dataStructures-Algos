class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.currSum = 0

        def dfs(node):
            if not node:
                return 0

            dfs(node.right)
            tmp = self.currSum
            node.val += self.currSum
            self.currSum = node.val
            dfs(node.left)
            return node
        return dfs(root)
