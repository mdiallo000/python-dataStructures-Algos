from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()
