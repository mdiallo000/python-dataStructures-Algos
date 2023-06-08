

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from email.policy import default
import re


class Solution:
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        # This problem can be solved utilizing the same method used in finding the level order traversal of a binary tree
        # This time however there is a small twist to it
        # It would be really easy to just put the right child of the each node into the queue but that wouldn't really work
        # Thus far i sort of confused as to how i may proceed
        #  okay my initial intuition is off since we dont actually need to consider the initilial test case i previously taught we had to look out for
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            size = len(q)
            right = None

            for _ in range(size):
                node = q.popleft()
                if node:
                    right = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if right:
                res.append(right)

        return res
