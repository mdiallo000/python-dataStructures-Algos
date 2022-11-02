from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append(root)
        res = [0]
        while q:
            size = len(q)
            levels = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    q.append(node.right)
                    q.append(node.left)
                    levels.append(node.val)
            if levels:
                res[0] = levels
        return res[0][-1]

    def findBottomLeftValue(self, root):

        self.maxHeigh = 0
        self.res = root.val

        def dfs(node, currHeight):
            if not node:
                return
            dfs(node.left, currHeight + 1)
            self.maxHeight = max(self.maxHeight, currHeight)
            if self.maxHeigh > currHeight:
                self.res = Node.val
            dfs(node.right, currHeight + 1)
        dfs(root, 0)
        return self.res
