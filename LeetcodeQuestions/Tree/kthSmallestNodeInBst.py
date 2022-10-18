class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        DFS(root)
        return self.res

        def DFS(root):
            if not root:
                return None
            DFS(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            DFS(root.right)
