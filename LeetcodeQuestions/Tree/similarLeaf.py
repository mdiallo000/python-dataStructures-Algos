from logging import root


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def determine(root1, root2):
            if not root and not root2:
                return True
            elif root2 and root1:
                return (root1.val == root2.val and determine(root1.left, root2.right) and determine(root1.right, root2.right))
            else:
                return False
        sum1 = [0]
        sum2 = [0]

        def similarTree(root, s):
            if not root.left and not root.right:
                s[0] += root.val
                return
            similarTree(root.left, s)
            similarTree(root.right, s)
            return s
        similarTree(roo1, sum1)
        similarTree(root2, sum2)
