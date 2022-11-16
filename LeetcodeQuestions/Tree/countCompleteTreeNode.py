class Solution:
    def countNodes(self, root):
        self.count = 0

        def dfs(node):
            if node:
                self.count += 1
                dfs(node.left)
                dfs(node.right)
            else:
                return
        dfs(root)
        return self.count

    def Optimal(self, root):
        pass
