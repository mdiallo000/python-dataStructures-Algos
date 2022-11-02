class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self) -> int:

        return self.res.pop(0)

    def hasNext(self) -> bool:
        if self.res:
            return True
        return False
