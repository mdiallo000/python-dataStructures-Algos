from turtle import right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root]

        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            #  check to make sure its not negative
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], left_max, right)

            return node.val + max(node.left, node.right)
