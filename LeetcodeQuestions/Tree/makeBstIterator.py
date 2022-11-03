class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.pos = 0

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self) -> int:

        res = self.res[self.pos]
        self.pos += 1
        return res

    def hasNext(self) -> bool:
        if self.pos <= len(self.res):
            return True
        return False
