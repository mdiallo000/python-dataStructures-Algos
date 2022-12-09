class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(node, currMin, currMax):
