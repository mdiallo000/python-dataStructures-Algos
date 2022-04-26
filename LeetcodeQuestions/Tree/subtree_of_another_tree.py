

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to validate first wether where we currently are
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

        def isSame(self, p, t):
            if not p and t:
                return True

            if p and t and t.val == p.val:
                return self.isSame(p.left, t.left) and self.isSame(p.right, t.right)
            return False
