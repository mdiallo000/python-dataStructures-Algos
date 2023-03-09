
from collections import deque


class Solution:
    def levelOrder(root):
        res = []
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    for child in node.children:
                        q.append(child)
                    level.append(node.val)
            if level:
                res.append(level)
        return res
