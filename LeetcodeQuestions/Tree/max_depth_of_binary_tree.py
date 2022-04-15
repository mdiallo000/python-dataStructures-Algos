

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from unittest import result


class Solution:
    def maxDepth_recursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        result = []
        queue = collections.deque()
        queue.append(root)

        while(queue):
            lenght = len(queue)
            level = []
            for i in range(lenght):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        return len(result)
