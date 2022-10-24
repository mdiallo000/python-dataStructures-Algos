class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def determine(subtree1, subtree2):
            if not subtree1 and not subtree2:
                return True
            elif subtree1 and subtree2:
                return (subtree1.val == subtree2.val and determine(subtree1.left, subtree2.right) and determine(subtree1.right, subtree2.left))
            else:
                return False

        return determine(root.left, root.right)
