from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            leftmost = None
            for _ in range(size):
                node = q.popleft()

                if node:
