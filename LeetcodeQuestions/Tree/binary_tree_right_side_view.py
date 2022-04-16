

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            lenght = len(queue)
            node = 0
            for i in range(lenght):
                node = queue.popleft()
