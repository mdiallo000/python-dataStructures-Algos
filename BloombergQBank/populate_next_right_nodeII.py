from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque()
        q.append(root)
