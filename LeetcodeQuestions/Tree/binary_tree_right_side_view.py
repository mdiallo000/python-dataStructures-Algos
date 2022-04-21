

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import re


class Solution:
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        #    result array
        result = []
        queue = collections.deque()
        queue.append(root)
    #  lets loop while there are still elements in our queue
        while queue:
            # lets get the length of the queue since we are only interested in looping at most each level
            queue_length = len(queue)
    #  lets keep track of the rightmost node in our queue, this is what we are interested in
            right_side = None
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side:
                result.append(right_side.val)
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        right = self.rightSideView(root.right)
        result.append(right)
        return result
