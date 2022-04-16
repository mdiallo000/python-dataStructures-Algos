

from turtle import right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], left, right)

            return 1+max(left, right)
        dfs(root)
        return res[0]
