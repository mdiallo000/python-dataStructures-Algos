class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root]

        def dfs(node):
            if not node:
                return 0
