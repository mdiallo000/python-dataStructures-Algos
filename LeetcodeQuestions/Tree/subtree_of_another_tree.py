

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to validate first wether where we currently are
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        def isSame(self, root, subRoot):
            if not root and subRoot:
                return True

            if root and subRoot and root.val == subRoot.val:
                return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
            return False
