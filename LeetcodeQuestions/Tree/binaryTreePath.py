class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []
        output = []

        def helper(root, curr):

            if not root:
                return

            if not root.left and not root.right:
                output.append('->'.join(curr + [str(root.val)]))
                return

            helper(root.left, curr + [str(root.val)])
            helper(root.right, curr + [str(root.val)])
        helper(root, [])
        return output
