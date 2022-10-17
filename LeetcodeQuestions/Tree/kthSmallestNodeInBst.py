class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k-1
        self.res = None
        dfs(root)
        return self.res

        def DFS(root):
            if not root
