

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
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(sum_level/queue_length)
        return res
# Time Complexity of O(n) since we visit every node to get its value.
# Space Complexity of O(n) as well since it may grow proportional to the size of the input array.
