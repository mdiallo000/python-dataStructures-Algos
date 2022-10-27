class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.pos = 0
        self.res = None

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.pos += 1
            if self.pos == k:
                self.res = node.val
