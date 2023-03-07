

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #  we need to recursively continue to delete nodes with the target value until we can no longer do so.
