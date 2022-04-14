# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root

        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
