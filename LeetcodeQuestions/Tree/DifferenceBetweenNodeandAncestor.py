class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(node, currMin, currMax):
            if not node:
                return

            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)
            self.res = max(self.res, abs(currMax - node.val),
                           abs(currMin - node.val))
            dfs(node.left, currMin, currMax)
            dfs(node.right. currMin, currMax)
            return
        dfs(root, root.val, root.val)
        return self.res
