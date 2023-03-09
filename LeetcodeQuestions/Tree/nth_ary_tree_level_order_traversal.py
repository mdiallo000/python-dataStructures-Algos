
from collections import deque


class Solution:
    def levelOrder(root):
        res = []
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            for _ in range(size):
