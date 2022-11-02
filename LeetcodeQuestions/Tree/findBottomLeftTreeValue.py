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
