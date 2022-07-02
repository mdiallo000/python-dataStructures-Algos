from collections import deque
from email.policy import default


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        columTable = default(list)
        q = deque()
        q.append([(root, 0)])
        result = []

        while q:
            size = len(q)
            for i in range(size):
                node, columPos = q.popleft()

                if node:
                    columTable[columPos].append(node.val)
                    q.append([(node.left, columPos - 1)])
                    q.append([(node.right, columPos + 1)])
        return [columTable[x] for x in sorted(key=columTable.keys())]
