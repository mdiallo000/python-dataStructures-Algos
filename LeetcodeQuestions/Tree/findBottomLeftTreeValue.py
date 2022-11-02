from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append(root)
        res = None
        while q:
            size = len(q)
            leftmost = None
            for _ in range(size):
                node = q.popleft()

                if node:
                    q.append(node.right)
                    q.append(node.left)
                    leftmost = node.val
            if leftmost:
                res = leftmost
        return res
