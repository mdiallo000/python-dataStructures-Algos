

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # An efficient way of solving this problem is to create a helper function which create boundaries within a node can be a Valid BST
        def validate(node, left_boundary, right_boundary):

            if not node:
                return True

            if not (node.val > left_boundary and node.val < right_boundary):
                return False
            return validate(node.left, left_boundary, node.val) and validate(node.right, node.val, right_boundary)
        return validate(root, float("-inf"), float("inf"))
