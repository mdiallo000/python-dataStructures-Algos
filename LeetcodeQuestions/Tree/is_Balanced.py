

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):

            if not root:
                return (0, True)

            l_height, l_balanced = helper(node.left)
            r_height, r_balanced = helper(node.right)

            return (max(l_height, r_height), l_balanced and r_balanced and abs(l_height-r_balanced) <= 1)

        return helper(root)[-1]
