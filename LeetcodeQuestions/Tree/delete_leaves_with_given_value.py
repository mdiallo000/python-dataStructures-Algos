

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #  we need to recursively continue to delete nodes with the target value until we can no longer do so.
