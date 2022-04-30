

import collections
from gc import collect


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_length = len(queue)
            sum_level = 0
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    sum_level += node.val
                    queue.append(node.left)
                    queue.append(node.right)
            res.append(sum_level//queue_length)
        return res
