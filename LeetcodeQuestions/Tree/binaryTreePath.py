class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []

        def dfs(node, curr):
            if not node.left and not node.right:
                curr.append(str(node.val))
                res.append(curr)
                return
            curr.append(str(node.val) + "=>")
            dfs(node.left, curr)
            curr.pop()
            dfs(node.right)
            return
        dfs(root, [])
        return res
