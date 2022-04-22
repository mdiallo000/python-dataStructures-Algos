

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
                return [True, 0]
            left = helper(node.left)
            right = helper(node.right)
            balance = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return [balance, 1+max(left[1], right[1])]

        return helper(root)[0]
